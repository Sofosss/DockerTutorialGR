FROM python:latest

RUN pip3 install --upgrade pip
RUN pip3 install uvicorn fastapi[all] motor python-jose[cryptography] 

# Passing sensitive data this way as well as tracking it in version control is a really bad idea.
# Use docker secrets or a similar solution instead.
ENV MONGODB_HOST="mongodb_node"
ENV MONGODB_HOST_PORT=27017
ENV DBNAME="CaseStudy3"
ENV SECRET_KEY="xj3zTIYDtc"
ENV LOGS_PATH="/var/log/webserver/requests_activity.log"

WORKDIR /opt/webserver
COPY . .


VOLUME ["/var/log/webserver/"]
EXPOSE 8891


ENTRYPOINT ["uvicorn","server:app","--reload","--host","0.0.0.0","--port","8891"]
