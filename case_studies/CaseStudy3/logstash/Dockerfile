# Use the official Logstash image from Elastic
FROM docker.elastic.co/logstash/logstash:8.12.2

# Install the Logstash output plugin for MongoDB
RUN logstash-plugin install logstash-output-mongodb

# Copy the Logstash configuration file to the appropriate directory
COPY logstash.conf /usr/share/logstash/pipeline/logstash.conf

# Expose the Logstash monitoring port
EXPOSE 9600

# Set the command to start Logstash with the specified configuration file
CMD ["logstash", "-f", "/usr/share/logstash/pipeline/logstash.conf"]