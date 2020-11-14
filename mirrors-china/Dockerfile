FROM node:lts-alpine as build0

COPY . /mirrors/

WORKDIR /mirrors

RUN npm install  && \
    npm run build


FROM nginx:alpine

COPY --from=build0 /mirrors/docs /usr/share/nginx/html
