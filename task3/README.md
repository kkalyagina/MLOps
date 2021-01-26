```
docker-compose build \
--build-arg USER_ID=$(id -u) \
--build-arg GROUP_ID=$(id -g) 
```

```
docker-compose run -v $(pwd)/Volume:/home/ mlflow-server bash
```

```
docker-compose up
```

```
docker-compose run {service_name} bash
```