FROM node:lts-slim

EXPOSE 3000

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .

RUN npm install

CMD ['npm', 'start']