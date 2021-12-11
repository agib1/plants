FROM node:lts-alpine as build

WORKDIR /app
COPY ./frontend/plantsapp/package*.json ./
RUN npm cache verify
RUN npm install
COPY ./frontend/plantsapp/ .
RUN npm run build

FROM nginx:stable-alpine as production
COPY ./nginx/prod.conf /etc/nginx/nginx.conf
COPY ./backend/static/ /usr/src/app/static/
COPY --from=build /app/dist /dist/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]