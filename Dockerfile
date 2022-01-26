FROM node:16 AS frontend-build
COPY frontend/package.json .
COPY frontend/yarn.lock .
RUN yarn install --pure-lockfile
COPY frontend/ .
RUN yarn run build


FROM python:3.9 as django-build

RUN apt-get update && apt-get install -y gettext

COPY backend/requirements.txt /app/backend/requirements.txt
RUN pip install --no-deps --no-cache-dir -r /app/backend/requirements.txt

WORKDIR /app/
COPY . /app/
# copies over the compiled sources from node image above
COPY --from=frontend-build /dist /app/frontend/dist

RUN python manage.py collectstatic --noinput --ignore=node_modules
RUN python manage.py compilemessages


ENV PORT=80
CMD uwsgi --http=0.0.0.0:$PORT --module=backend.wsgi --master --workers=4 --max-requests=1000 --lazy-apps --need-app --http-keepalive --harakiri 65 --vacuum --strict --single-interpreter --die-on-term --disable-logging --log-4xx --log-5xx --cheaper=2 --enable-threads 
# some explanations
# --strict means that uwsgi will quit if the app cannot startup, respectively throws an error on startup. That's convenient because of clear log entries.
# the number of workers depend on how many CPU cores and how much memory the server has. For example, on a 4 core with 4GB RAM, if one worker takes 200MB of RAM, you can try 4 to 8 workers.
# see https://www.techatbloomberg.com/blog/configuring-uwsgi-production-deployment/ to explain some of these settings
# https://uwsgi-docs.readthedocs.io/en/latest/articles/TheArtOfGracefulReloading.html#preforking-vs-lazy-apps-vs-lazy
