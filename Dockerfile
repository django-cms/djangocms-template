# <WARNING>
# Everything within sections like <TAG> is generated and can
# be automatically replaced on deployment. You can disable
# this functionality by simply removing the wrapping tags.
# </WARNING>

# <DOCKER_FROM>
FROM divio/base:4.15-py3.6-slim-stretch
# </DOCKER_FROM>

# <BACKEND>
ENV PIP_INDEX_URL=${PIP_INDEX_URL:-https://wheels.aldryn.net/v1/aldryn-extras+pypi/${WHEELS_PLATFORM:-aldryn-baseproject-py3}/+simple/} \
    WHEELSPROXY_URL=${WHEELSPROXY_URL:-https://wheels.aldryn.net/v1/aldryn-extras+pypi/${WHEELS_PLATFORM:-aldryn-baseproject-py3}/}
COPY requirements.* /app/
COPY addons-dev /app/addons-dev/
RUN pip install requirements.txt
# </BACKEND>

# <SOURCE>
COPY . /app
# </SOURCE>

# <FRONTEND>
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
RUN yarn install --pure-lockfile
RUN yarn run build
RUN DJANGO_MODE=build python manage.py collectstatic --noinput
# </FRONTEND>
