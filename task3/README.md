# MlFlow

To build an image:
```
docker-compose build \
--build-arg USER_ID=$(id -u) \
--build-arg GROUP_ID=$(id -g) 
```

To run containers from the image:
```
docker-compose up
```

```
docker-compose run -v $(pwd)/Volume:/home/ mlflow-server bash
```

```
docker-compose run {service_name} bash
```
