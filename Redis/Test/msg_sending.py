import redis
import time
import random
import string

# Redis Configuration
REDIS_HOST = 'localhost'
REDIS_PORT = 6378
STREAM_NAME = 'mystream'

# Initialize Redis Client
r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)

# Function to generate a random string (message)
def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Sending messages to Redis Stream
try:
    while True:
        message = random_string()  # Generate random string
        # Add message to the Redis stream
        r.xadd(STREAM_NAME, {'message': message})
        print(f"Sent message: {message}")
        time.sleep(5)  # Simulating slow message sending
except KeyboardInterrupt:
    print("\nStopping producer...")
