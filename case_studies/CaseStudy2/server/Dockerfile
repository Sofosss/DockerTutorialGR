# This Dockerfile sets up a Node.js environment and runs a server using Express and body-parser.
# It exposes port 8891 and starts the server by running the "server.js" file, waiting for incoming requests.

# Use the latest Node.js image as the base image.
FROM node:latest 

# Set metadata labels for the image.
LABEL maintainer="Argiris Sofotasios & Dimitris Metaxakis"
LABEL description="A simple Web app."

# Set environment variables.
ENV NODE_PORT=8899
ENV VOLUME_DIR="/opt/user_data"

# Set the working directory inside the container.
WORKDIR /app

# Copy the current directory contents into the container at /app.
COPY . /app

# Install the required Node.js packages.
RUN npm install express body-parser path

# Expose port 8891 to allow external access.
EXPOSE 8891

# Define the command to run the application when the container starts.
ENTRYPOINT ["node", "server.js"]

#curl -X POST -H "Content-Type: application/json" -d '{"name":"George", "address":"Artakis 77"}' 127.0.0.1:32768