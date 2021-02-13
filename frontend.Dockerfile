FROM registry.gitlab.com/what-digital/djangocms-template:3.0

WORKDIR /app/frontend/
COPY frontend/package.json .
COPY frontend/yarn.lock .
RUN yarn install --pure-lockfile
