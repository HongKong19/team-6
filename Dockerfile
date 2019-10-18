FROM node:12.10.0-alpine
WORKDIR /app
COPY . .
RUN npm install
ADD . /app

EXPOSE 8080
CMD npm run serve