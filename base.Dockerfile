FROM divio/base:1.0-py3.9-slim-buster


RUN apt update --quiet
RUN apt install --yes \
    # for pip installing git repositories
    git gnupg2 apt-transport-https \
    fish \
    nano \
    # for building node modules & python packages
    gcc build-essential \
    # for building psycopg2
    libpq-dev


RUN pip install --upgrade pip
RUN apt --yes upgrade


# yarn
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update --quiet && apt-get install --yes yarn nodejs


# fish
RUN usermod -s /usr/bin/fish root
RUN curl -L https://get.oh-my.fish > fish-install
RUN fish fish-install --noninteractive --yes


# divio envs
ENV PIP_INDEX_URL=${PIP_INDEX_URL:-https://wheels.aldryn.net/v1/aldryn-extras+pypi/${WHEELS_PLATFORM:-aldryn-baseproject-py3}/+simple/} \
    WHEELSPROXY_URL=${WHEELSPROXY_URL:-https://wheels.aldryn.net/v1/aldryn-extras+pypi/${WHEELS_PLATFORM:-aldryn-baseproject-py3}/}
