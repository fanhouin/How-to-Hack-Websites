FROM node:latest
WORKDIR /app

COPY ./ /app
RUN npm install --no-bin-links

RUN ["chmod", "+x", "./start.sh"]
CMD [ "npm", "start" ]
