FROM registry.gitlab.com/what-digital/djangocms-template:3.0


COPY backend/requirements.txt /app/backend/requirements.txt
RUN pip install --no-deps --no-cache-dir -r /app/backend/requirements.txt


WORKDIR /app/frontend/
COPY frontend/package.json .
COPY frontend/yarn.lock .
RUN yarn install --pure-lockfile
COPY frontend/ /app/frontend/
RUN yarn run build


WORKDIR /app/
COPY . /app/


ENV STAGE='build_docker'
RUN python manage.py collectstatic --noinput --ignore=node_modules
RUN python manage.py compilemessages --ignore=node_modules


ENV PORT=80
CMD uwsgi --http=0.0.0.0:$PORT --module=backend.wsgi
