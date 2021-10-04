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
RUN python manage.py compilemessages --ignore=node_modules


ENV PORT=80
CMD uwsgi --http=0.0.0.0:$PORT --module=backend.wsgi
