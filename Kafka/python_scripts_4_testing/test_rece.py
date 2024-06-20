from kafka import KafkaConsumer

# set up the Kafka consumer
consumer = KafkaConsumer(
    'topic-sample-two', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')

# consume messages from the 'test' topic
for message in consumer:
    print(message.value.decode('utf-8'))
