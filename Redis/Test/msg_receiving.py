import redis
import time

# Redis Configuration
REDIS_HOST = 'localhost'
REDIS_PORT = 6378
STREAM_NAME = 'mystream'

# Initialize Redis Client
r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

# Consumer Group Name
GROUP_NAME = 'mygroup'
CONSUMER_NAME = 'consumer1'

# Create a consumer group if it does not exist
try:
    r.xgroup_create(STREAM_NAME, GROUP_NAME, id='0', mkstream=True)
except redis.exceptions.ResponseError as e:
    # Group already exists, ignore error
    print(f"Group '{GROUP_NAME}' already exists.")

def process_message(msg_id, data):
    message_value = data.get(b'message').decode('utf-8')
    print(f"Received message: {message_value}")
    # Acknowledge the message
    r.xack(STREAM_NAME, GROUP_NAME, msg_id)
    time.sleep(1)  # Simulating slow processing

# Process pending messages on startup
print("Checking for pending messages...")
try:
    while True:
        # Fetch pending messages (up to 100 at a time)
        pending_response = r.xreadgroup(
            groupname=GROUP_NAME,
            consumername=CONSUMER_NAME,
            streams={STREAM_NAME: '0'},
            count=100,
            block=0
        )

        stream, messages = pending_response[0]
        for message in messages:
            if not message:
                print("Finished processing pending messages.")
                break  # break the first while loop | empty message

            msg_id, msg_data = message
            process_message(msg_id, msg_data)
        print("Finished processing pending messages.")
        break # break the first while loop | Finished processing
    
    # This is the second while loop, which will keep listening for new messages
    while True:
        # Read new messages with blocking call
        messages = r.xreadgroup(
            GROUP_NAME,
            CONSUMER_NAME,
            {STREAM_NAME: '>'},
            block=1000,
            count=10
        )
        if not messages:
            print("No new messages. Waiting...")
            continue
        # print("second while loop")
        stream, messages = messages[0]
        for message in messages:
            msg_id, msg_data = message
            process_message(msg_id, msg_data)

except KeyboardInterrupt:
    print("\nStopping consumer...")