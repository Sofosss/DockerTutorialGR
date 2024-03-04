FROM python:latest

# Upgrade pip and install necessary Python packages
RUN pip3 install --upgrade pip
RUN pip3 install uvicorn fastapi[all] motor python-jose[cryptography] 

# Passing sensitive data this way as well as tracking it in version control is a really bad idea.
# Use docker secrets or a similar solution instead.
ENV MONGODB_HOST="mongodb_node"
ENV MONGODB_HOST_PORT=27017
ENV DBNAME="CaseStudy3"
ENV SECRET_KEY="xj3zTIYDtc"
ENV LOGS_PATH="/var/log/webserver/requests_activity.log"

# Set the working directory to /opt/webserver
WORKDIR /opt/webserver

# Copy the application files into the container
COPY . .

# Create a volume for storing log files
VOLUME ["/var/log/webserver/"]

# Expose the application's port
EXPOSE 8891

# Define the entry point for running the application
ENTRYPOINT ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0", "--port", "8891"]









