# <WARNING>
# Everything within sections like <TAG> is generated and can
# be automatically replaced on deployment. You can disable
# this functionality by simply removing the wrapping tags.
# </WARNING>

FROM registry.gitlab.com/what-digital/djangocms-template:latest


COPY requirements.* /app/
COPY addons-dev /app/addons-dev/
RUN pip-reqs resolve && \
    pip install \
        --no-index --no-deps \
        --requirement requirements.urls


# <SOURCE>
COPY . /app
# </SOURCE>


# FRONTEND
# for yarn
RUN yarn install --pure-lockfile
RUN yarn run build
RUN DJANGO_MODE=build python manage.py collectstatic --noinput
