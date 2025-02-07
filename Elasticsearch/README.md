# Elasticsearch & Kibana Docker Compose Setup

This repository provides a simple setup for running Elasticsearch and Kibana using Docker Compose, based on the official [Elasticsearch Docker documentation](https://www.elastic.co/guide/en/elasticsearch/reference/8.5/docker.html).

## Prerequisites

1. Ensure you have Docker and Docker Compose installed on your local machine.
2. Create a `.env` file from the `.env.sample` file in the root directory. This file contains environment variables necessary for the configuration.

## Stack Version Tested

- Elasticsearch: 8.5.3
- Kibana: 8.5.3

## Running the Stack

To spin up the Elasticsearch cluster along with Kibana, follow these steps:

1. Make sure you have the `.env` file in place (from `.env.sample`).
2. Navigate to the directory containing the `docker-compose.yml` file.
3. Execute the following command to start the services:

   ```bash
   docker compose up -d
   ```

   This will pull the necessary Docker images and start Elasticsearch and Kibana in detached mode.

## Diff Type of cluster 

To spin the elasticsearch cluster 

1. Use cluster-docker-compose.yaml file to spin cluster setup with ssl certificates 
2. Use single-node-docker-compose.yaml file to spin single node cluster without any security features

   ```bash
   docker compose -f cluster-docker-compose.yaml up -d
   ```

   ```bash
   docker compose -f single-node-docker-compose.yaml up -d
   ```

## Accessing Kibana

Once the services are up and running, access Kibana at:

```
http://localhost:5601
```

- **Username**: `elastic`
- **Password**: `your_password` (as defined in the `.env` file)

Use these credentials to log in to the Kibana console.

## Stopping the Stack

To stop the stack, run:

```bash
docker compose down
```

This will stop and remove the containers, networks, and volumes defined in the `docker-compose.yml` file.

## Notes

- Ensure your `.env` file contains the correct configurations, especially the `ELASTIC_PASSWORD` to log in to Kibana.
- This setup is designed for development and testing purposes. For production environments, please refer to the [official Elastic documentation](https://www.elastic.co/guide/en/elasticsearch/reference/index.html).
