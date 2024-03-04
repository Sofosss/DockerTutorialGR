# This Dockerfile sets up a Node.js environment and runs a server using Express and body-parser.
# It exposes port 8891 and starts the server by running the "server.js" file, waiting for incoming requests.

# Use the latest Node.js image from the official repository
FROM node:latest 

# Set the maintainers and description labels for the image
LABEL maintainer="Argiris Sofotasios & Dimitris Metaxakis"
LABEL description="A simple Web app."

# Set environment variables for Node.js application
ENV NODE_PORT=8891
ENV VOLUME_DIR="/opt/data_per"

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install necessary dependencies using npm
RUN npm install express body-parser path

# Expose port 8891 to allow external access to the application
EXPOSE 8891

# Specify the command to run the application when the container starts
ENTRYPOINT ["node", "server.js"]

#curl -X POST -H "Content-Type: application/json" -d '{"name":"George", "address":"Artakis 77"}' 127.0.0.1:32768