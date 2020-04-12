FROM registry.gitlab.com/what-digital/djangocms-template:latest


COPY . /app/


RUN pip-reqs resolve && pip install --no-index --no-deps --requirement requirements.urls


RUN yarn install --pure-lockfile
RUN yarn run build
RUN DJANGO_MODE=build python manage.py collectstatic --noinput
