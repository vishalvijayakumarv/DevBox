# Jenkins Docker Compose Setup

This project sets up Jenkins using Docker Compose, with persistent configuration stored in the `jenkins_home` folder.

## Setup

1. **Clone this repository** (if needed).

2. **Ensure Docker and Docker Compose are installed** on your machine.

3. **Folder Structure**:
   - The `jenkins_home` folder holds all Jenkins configurations and is mounted as a volume inside the Jenkins Docker container.

## Running Jenkins

To start Jenkins:

```bash
docker-compose up -d
```

After the container is up, Jenkins will be accessible via the following URL:
- **Jenkins URL**: [http://localhost:8080](http://localhost:8080)

## Getting the Jenkins Admin Token

To retrieve the Jenkins admin token (for first-time login), run the following command:

```bash
docker logs -f jenkins-master
```

You will see the admin token displayed in the logs. Copy the token for login.

## Customizing the Jenkins Master Docker Container

If you need to install additional tools inside the Jenkins master container (e.g., Ansible), you can do so by editing the `Dockerfile`.

Once you've updated the Dockerfile, rebuild the container:

```bash
docker-compose up -d --build
```

## Accessing Jenkins Dashboard

Once Jenkins is running, open your browser and visit:

- **Dashboard URL**: [http://127.0.0.1:8080](http://127.0.0.1:8080)

## Stopping Jenkins

To stop Jenkins, run:

```bash
docker-compose down
```

This will stop the containers and remove them.

## Volumes and Data Persistence

- The `jenkins_home` folder persists Jenkins data across container restarts.
- You can back up and restore Jenkins data by managing the contents of this folder.

## Troubleshooting

- If Jenkins is not starting or facing issues, check the logs:

```bash
docker logs jenkins-master
```
