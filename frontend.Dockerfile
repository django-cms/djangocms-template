FROM registry.gitlab.com/what-digital/djangocms-template:latest

COPY package.json /app/package.json
COPY yarn.lock /app/yarn.lock
COPY frontend/ /app/frontend/

RUN yarn install --pure-lockfile
