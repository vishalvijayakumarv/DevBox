# Kafka Docker Setup

## Overview
This is a custom Kafka setup using Docker containers. **Note**: This is not an official Kafka image or setup. The following Docker images are used:
- `wurstmeister/kafka`
- `zookeeper`

## Getting Started

### Prerequisites
- Docker and Docker Compose installed on your system.

### Running the Containers
To start the containers, run the following command:
```bash
docker compose up -d
```

This will start:
1. A Zookeeper container on port `2181`.
2. A Kafka container on port `9092`.

### Default Configuration
- By default, this setup creates **two Kafka topics**:
  - `topic-sample-one`: 1 partition, replication factor 1
  - `topic-sample-two`: 2 partitions, replication factor 1

## Testing Kafka
To test the Kafka setup, use the Python scripts located in the `Test` folder. These scripts can:
1. **Send Data**  `Test\produce.py` to Kafka topics.
2. **Read Data** `Test\consume.py` from Kafka topics.

### Note:
Ensure the topics in your scripts match the topics defined in the Docker Compose file (`topic-sample-one`, `topic-sample-two`).

## Additional Information
- This setup is for local testing and development purposes.
- For production, consider using official images and a more secure configuration.
