import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2D, Dense, Flatten, Dropout, GlobalMaxPooling2D
from tensorflow.keras.models import Model

import os
import mlflow
from random import random, randint
from mlflow import log_metric, log_param, log_artifacts #pyfunc
import mlflow.tensorflow

print(tf.__version__)

if __name__ == "__main__":
    # Log a parameter (key-value pair)
    mlflow.set_tracking_uri("http://0.0.0.0:7777") #mlflow-server:7777
  # mlflow.set_experiment("/my-experiment")
    
    log_param("param1", randint(0, 100))

    # Log a metric; metrics can be updated throughout the run
    log_metric("foo", random())
    log_metric("foo", random() + 1)
    log_metric("foo", random() + 2)


# Load in the data
fashion_mnist = tf.keras.datasets.fashion_mnist

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Increase one dimension so it can be used by the 2D convolutional keras layer
x_train = np.expand_dims(x_train,-1)
x_test = np.expand_dims(x_test,-1)
print("x_train.shape:", x_train.shape)

# Run the model
mlflow.tensorflow.autolog()

def run_model(params):
  with mlflow.start_run(run_name="tracking experiment") as run:
    # number of classes
    K = len(set(y_train))
    print("number of classes:", K)
    # Build the model using the functional API
    i = Input(shape=x_train[0].shape)
    x = Conv2D(32, params['convSize'], strides=2, activation='relu')(i)
    x = Conv2D(64, params['convSize'], strides=2, activation='relu')(x)
    x = Conv2D(128, params['convSize'], strides=2, activation='relu')(x)
    x = Flatten()(x)
    x = Dropout(0.2)(x)
    x = Dense(512, activation='relu')(x)
    x = Dropout(0.2)(x)
    x = Dense(K, activation='softmax')(x)

    model = Model(i, x)

    # Compile and fit
    # Note: make sure you are using the GPU for this!
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    r = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=params['epochs'])
    return (run.info.experiment_id, run.info.run_id)
    
for epochs, convSize in [[3,2], [15,3]]:
  params = {'epochs': epochs,
            'convSize': convSize}
  run_model(params)

