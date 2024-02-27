FROM ubuntu:latest

LABEL maintainer="Argiris Sofotasios & Dimitris Metaxakis"
LABEL description="A client that makes http requests to the server container."

RUN apt-get update && apt-get install -y curl jq


ENV SERVER_NAME="node_server"
ENV SERVER_PORT="8899"

WORKDIR /request
COPY . /request

ENTRYPOINT [ "bash","fetch_req.sh" ]
