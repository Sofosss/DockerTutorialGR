FROM docker.elastic.co/logstash/logstash:8.12.2


RUN logstash-plugin install logstash-output-mongodb

COPY logstash.conf /usr/share/logstash/pipeline/logstash.conf

EXPOSE 9600

CMD ["logstash", "-f", "/usr/share/logstash/pipeline/logstash.conf"]