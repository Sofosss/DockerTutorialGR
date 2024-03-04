# Dockerfile for setting up MongoDB with authentication and a specific database

# Use the latest official MongoDB image as the base image
FROM mongo:latest

# Set environment variables for MongoDB initialization
ENV MONGO_INITDB_ROOT_USERNAME="admin" 
ENV MONGO_INITDB_ROOT_PASSWORD="dummyPassword123"
ENV MONGO_INITDB_DATABASE="CaseStudy3"


# Copy the initialization script (init.js) to the container's init directory
COPY init.js /docker-entrypoint-initdb.d/

# Expose the default MongoDB port (27017) to allow external connections
EXPOSE 27017

# Set the default command to start MongoDB and bind it to all network interfaces
CMD ["mongod", "--bind_ip_all"]
