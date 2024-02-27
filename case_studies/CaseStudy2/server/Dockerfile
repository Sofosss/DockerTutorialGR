# This Dockerfile sets up a Node.js environment and runs a server using Express and body-parser.
# It exposes port 8891 and starts the server by running the "server.js" file, waiting for incoming requests.

FROM node:latest 

LABEL maintainer="Argiris Sofotasios & Dimitris Metaxakis"
LABEL description="A simple Web app."

ENV NODE_PORT=8899
ENV VOLUME_DIR="/opt/user_data"

WORKDIR /app
COPY . /app

RUN npm install express body-parser path

EXPOSE 8891

ENTRYPOINT ["node", "server.js"]

#curl -X POST -H "Content-Type: application/json" -d '{"name":"George", "address":"Artakis 77"}' 127.0.0.1:32768