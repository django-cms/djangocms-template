FROM registry.gitlab.com/what-digital/djangocms-template:latest

COPY package.json /app/package.json
COPY yarn.lock /app/yarn.lock

RUN yarn install --pure-lockfile
