FROM node:14
WORKDIR /app/frontend
COPY frontend/package.json .
COPY frontend/yarn.lock .
RUN yarn install --pure-lockfile
RUN yarn global add webpack-dev-server webpack
