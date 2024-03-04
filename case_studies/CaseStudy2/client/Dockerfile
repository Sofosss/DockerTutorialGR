# Dockerfile for a client making HTTP requests to a server container.

# Use the latest Ubuntu image from the official repository
FROM ubuntu:latest

# Set the maintainers and description labels for the image
LABEL maintainer="Argiris Sofotasios & Dimitris Metaxakis"
LABEL description="A client that makes http requests to the server container."

# Update the package list and install necessary tools (curl and jq)
RUN apt-get update && apt-get install -y curl jq

# Set environment variables for server information
ENV SERVER_NAME="node_server"
ENV SERVER_PORT="8899"

# Set the working directory inside the container
WORKDIR /request

# Copy the contents of the current directory into the container at /request
COPY . /request

# Specify the command to run when the container starts
ENTRYPOINT [ "bash", "fetch_req.sh" ]
