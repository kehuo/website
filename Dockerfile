FROM node:10
COPY ./ /app
WORKDIR /app
RUN yarn install && yarn docs:build

FROM nginx
RUN mkdir /app
COPY --from=0 /app/docs/.vuepress/dist /app

VOLUME [ "/etc/nginx/nginx.conf" ]
