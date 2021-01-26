FROM python:3.7-slim

RUN pip install mlflow

ARG USER_ID
ARG GROUP_ID

EXPOSE 7777

# Creating an user and a group

RUN addgroup --gid $GROUP_ID mlflow_task3
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID mlflow_task3

# Switch to new user 'mlflow_task3'

USER mlflow_task3

# Working directory

WORKDIR /home/mlflow_task3

CMD mlflow server \
    --host 0.0.0.0:7777
