FROM registry.gitlab.com/what-digital/djangocms-template:latest

WORKDIR /app/frontend/
COPY frontend/package.json /app/frontend/package.json
COPY frontend/yarn.lock /app/frontend/yarn.lock

RUN yarn install --pure-lockfile
