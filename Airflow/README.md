# Airflow Docker Compose Setup

## Default Credentials
- **Username:** `airflow`
- **Password:** `airflow`

## Volumes Created
When running the setup, the following directories will be created at the path of the `docker-compose.yaml` file:
1. `dags`
2. `logs`
3. `plugins`

## Environment Variables
- Copy `.env.sample` to `.env` and update the file with the required credentials.
- If no changes are made, the default values from `.env.sample` will be used.

## Starting the Docker Containers
To spin up the containers, simply run:
```bash
docker compose up -d
```

## Adding or Modifying DAGs
- If you add or modify any DAGs in the `dags` folder, ensure the `airflow-init` container has run at least once.
- To manually run the `airflow-init` container, execute:
```bash
docker compose up -d airflow-init
```

## Airflow Init Container
- The `airflow-init` container may exit after some time, which is expected behavior as it is equivalent to running the Airflow `init` command.

---
Follow these instructions to get your Airflow environment up and running efficiently!

