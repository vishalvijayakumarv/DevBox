from kafka import KafkaProducer
import time


# set up the Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# send a list of items to the 'test' topic
# items = ['item1', 'item2', 'item3']
items = list(range(30))
for item in items:
    print(item)
    time.sleep(1)
    print(f"item :{item} sending")
    if item % 3 == 0:
        producer.send('topic-sample-one', bytes(str(item), 'utf-8'))
        producer.flush()
        print(f"item :{item} sent")

# flush the messages to the Kafka broker
# producer.flush()
