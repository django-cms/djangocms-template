FROM divio/base:2.1-py3.9-slim-buster


RUN apt update --quiet
RUN apt install --yes \
    # for pip installing git repositories
    git gnupg2 apt-transport-https \
    fish \
    nano \
    # for building node modules & python packages
    gcc build-essential autoconf \
    # for webpack image loader
    libpng-dev \
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
