FROM registry.gitlab.com/what-digital/djangocms-template:1.1.0.7


COPY . /app/


RUN pip install -r requirements.txt


RUN yarn install --pure-lockfile
RUN yarn run build
RUN DJANGO_MODE=build python manage.py collectstatic --noinput

RUN python manage.py test_pages_on_real_db
