# Redis Docker Setup & Testing

## Description
This setup deploys a Redis server using Docker Compose and provides a Python script to test connectivity and data operations.

## Setup
1. Start Redis server:

   `docker-compose up -d`

2. Run the test script:

   `python redis_test.py`


## Features
- Redis server running on port `6379`.
- Data persistence with `appendonly` enabled.
- Python script tests connection and key-value operations.

