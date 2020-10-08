FROM divio/base:0.7-py3.7-slim-stretch

RUN apt-get update --quiet && apt-get install --yes git gnupg2 apt-transport-https gcc nano


# yarn
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update --quiet && apt-get install --yes yarn nodejs


# divio envs
ENV PIP_INDEX_URL=${PIP_INDEX_URL:-https://wheels.aldryn.net/v1/aldryn-extras+pypi/${WHEELS_PLATFORM:-aldryn-baseproject-py3}/+simple/} \
    WHEELSPROXY_URL=${WHEELSPROXY_URL:-https://wheels.aldryn.net/v1/aldryn-extras+pypi/${WHEELS_PLATFORM:-aldryn-baseproject-py3}/}


COPY . /app/


RUN pip install -r backend/requirements.txt


WORKDIR /app/


WORKDIR /app/frontend/
RUN yarn install --pure-lockfile
RUN yarn run build


WORKDIR /app/
RUN DJANGO_MODE=build python manage.py collectstatic --noinput
RUN DJANGO_MODE=build python manage.py compilemessages
