FROM node:13 as build-stage
WORKDIR /app
COPY . .
RUN yarn install && yarn build

FROM nginx
RUN mkdir /app && \
    rm /etc/nginx/nginx.conf
COPY --from=build-stage /app/docs/.vuepress/dist /app

EXPOSE 80
VOLUME [ "/etc/nginx/nginx.conf" ]
CMD ["nginx", "-g", "daemon off;"]
