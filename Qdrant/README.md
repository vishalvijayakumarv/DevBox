# Qdrant Docker Compose Setup

This repository provides a Docker Compose configuration to run [Qdrant](https://qdrant.tech/), a vector similarity search engine, using Docker.

## Prerequisites

- Docker installed on your system. [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose installed. [Install Docker Compose](https://docs.docker.com/compose/install/)

## Quick Start

1. Start the Qdrant service by running the following command in the directory containing the `docker-compose.yml` file:

   ```bash
   docker-compose up -d
   ```

   This will start the Qdrant container in detached mode.

2. Verify that the service is running by accessing the Qdrant dashboard at:

   - **HTTP API**: `http://localhost:6333`
   - **gRPC API**: `http://localhost:6334`

## Configuration

### Volumes

- The Qdrant data is persisted in a Docker volume named `qdrant_storage`. This ensures that your data is retained even if the container is stopped or removed.

### Networks

- The container is connected to a Docker network named `app-network`. This can be useful if you want to connect other services to the same network.

## References

- **Compatible Qdrant Versions**: For more compatible versions of the Qdrant Docker image, refer to the [Qdrant Docker Hub page](https://hub.docker.com/r/qdrant/qdrant/tags).
- **Connection Setup**: For detailed instructions on setting up and connecting to Qdrant, refer to the [Qdrant Quickstart Documentation](https://qdrant.tech/documentation/quickstart/).

## Stopping the Service

To stop the Qdrant service, run:

```bash
docker-compose down
```

This will stop and remove the container while preserving the data in the `qdrant_storage` volume.
