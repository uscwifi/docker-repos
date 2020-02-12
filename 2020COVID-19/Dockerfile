FROM node:lts-alpine

COPY 2020COVID-19  /app

WORKDIR /app

RUN npm config set registry https://registry.npm.taobao.org && \
  npm  install && \
  node scripts/build-origin.js

EXPOSE 5000


CMD [ "npm", "start" ]
