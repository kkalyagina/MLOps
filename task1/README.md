
To build a Docker image from Dockerfile:

```
docker build -t task1 \
--build-arg USER_ID=$(id -u) \
--build-arg GROUP_ID=$(id -g) .
```

To mount a directory from the host machine to the container and to run a container from Docker image:

```
docker run -v $(pwd)/Volume:/home/ task1
```