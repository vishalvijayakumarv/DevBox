# Start a producer that sends messages to the 'test' topic
#   docker-compose exec kafka kafka-console-producer.sh --broker-list localhost:9092 --topic test

# Start a consumer that reads messages from the 'test' topic
#   docker-compose exec kafka kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning

# to get topic list 
#   docker exec -it apachekafka-kafka-1 /opt/kafka/bin/kafka-topics.sh --list --bootstrap-server localhost:9092

# to describe the topic 
#   docker exec -it apachekafka-kafka-1 /opt/kafka/bin/kafka-topics.sh --describe --bootstrap-server localhost:9092  --topic topic-sample-two
