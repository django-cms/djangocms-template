FROM registry.gitlab.com/what-digital/djangocms-template:latest


COPY . /app/


RUN pip install -r backend/requirements.txt


WORKDIR /app/


WORKDIR /app/frontend/
RUN yarn install --pure-lockfile
RUN yarn run build


WORKDIR /app/
RUN DJANGO_MODE=build python manage.py collectstatic --noinput
RUN DJANGO_MODE=build python manage.py compilemessages
