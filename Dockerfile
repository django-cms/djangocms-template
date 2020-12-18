FROM registry.gitlab.com/what-digital/djangocms-template:3.0.0.0


COPY backend/requirements.txt /app/backend/requirements.txt
RUN pip install --no-deps --no-cache-dir -r /app/backend/requirements.txt


COPY frontend/ /app/frontend/
WORKDIR /app/frontend/
RUN yarn install --pure-lockfile
RUN yarn run build


WORKDIR /app/
COPY . /app/


RUN DJANGO_MODE=build python manage.py collectstatic --noinput --ignore=node_modules
RUN DJANGO_MODE=build python manage.py compilemessages


CMD uwsgi --http=0.0.0.0:$PORT --module=backend.wsgi
