import redis

def test_redis():
    try:
        # Connect to Redis
        client = redis.StrictRedis(host='localhost', port=6379, db=0)

        # Ping Redis to check the connection
        if client.ping():
            print("Connected to Redis!")

        # Set a key-value pair
        client.set("test_key", "Hello, Redis!")
        print("Data written to Redis")

        # Read the value back
        value = client.get("test_key").decode("utf-8")
        print(f"Data read from Redis: {value}")

    except redis.ConnectionError as e:
        print(f"Failed to connect to Redis: {e}")

if __name__ == "__main__":
    test_redis()
