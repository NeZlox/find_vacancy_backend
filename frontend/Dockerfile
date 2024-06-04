FROM node:latest AS builder

WORKDIR /client

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

# Отдельный этап для запуска Nginx
FROM nginx:alpine

COPY --from=builder /client/build /usr/share/nginx/html

COPY nginx.conf /etc/nginx/nginx.conf
CMD ["nginx", "-g", "daemon off;"]