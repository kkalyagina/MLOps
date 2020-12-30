FROM ubuntu:18.04


RUN apt-get update && apt-get install -yq git wget make g++ unzip 
                      

# Install Starspace

RUN wget https://dl.bintray.com/boostorg/release/1.63.0/source/boost_1_63_0.zip && \ 
    unzip boost_1_63_0.zip && \
    mv boost_1_63_0 /usr/local/bin && \
    git clone https://github.com/facebookresearch/Starspace.git && \
    cd Starspace && \
    make && \
    cp -Rf starspace /usr/local/bin


# Creating an user and a group

ARG USER_ID
ARG GROUP_ID

RUN addgroup --gid $GROUP_ID kris
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID kris

# Switch to new user 'kris'

USER kris

# Command to run the Starspace on input data


CMD cd Starspace && ./starspace train -trainFile /home/input.txt -model /home/output




