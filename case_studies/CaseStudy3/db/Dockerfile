FROM mongo:latest

ENV MONGO_INITDB_ROOT_USERNAME="admin" 
ENV MONGO_INITDB_ROOT_PASSWORD="dummyPassword123"
ENV MONGO_INITDB_DATABASE="CaseStudy3"

COPY init.js /docker-entrypoint-initdb.d/


EXPOSE 27017

CMD ["mongod", "--bind_ip_all"]
