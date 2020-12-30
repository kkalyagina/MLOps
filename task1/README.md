To build a Docker image from Dockerfile:

docker build -t ubuntu \
--build-arg USER_ID=$(id -u) \
--build-arg GROUP_ID=$(id -g) .


To mount a directory from the host machine to the container and to run a container from Docker image:

docker run -it -v /home/kkalyagina/Desktop/Docker/Volume:/home/ 47e9779

