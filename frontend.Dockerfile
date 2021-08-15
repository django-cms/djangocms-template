FROM node:16

COPY frontend/package.json /package.json
COPY frontend/yarn.lock /yarn.lock

RUN yarn install --pure-lockfile --modules-folder /node_modules
