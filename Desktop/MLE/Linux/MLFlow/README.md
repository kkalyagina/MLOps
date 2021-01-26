docker-compose build -t mlflow-server \
--build-arg USER_ID=$(id -u) \
--build-arg GROUP_ID=$(id -g) .

docker-compose run -v $(pwd)/Volume:/home/ mlflow-server bash
