from kafka import KafkaConsumer
from kafka.errors import KafkaError

# consumer = KafkaConsumer(
#     'topic-sample-one', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')


consumer = KafkaConsumer(
    'topic-sample-one',
    group_id='1001',
    bootstrap_servers=['localhost:9092']
)


for message in consumer:

    # Process the message here
    print(message.value)
    print(message)
    # Remove the message from the queue
    try:
        # consumer.commit()
        consumer.poll()
    except KafkaError as e:
        print("Failed to delete message from queue:", e)
