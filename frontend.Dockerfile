FROM registry.gitlab.com/what-digital/djangocms-template:latest

WORKDIR /app/frontend/
COPY package.json /app/frontend/package.json
COPY yarn.lock /app/frontend/yarn.lock

RUN yarn install --pure-lockfile

WORKDIR /app/
