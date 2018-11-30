# use base ubuntu 18
FROM ubuntu:18.04

# install some packages needed for example
RUN apt-get update \
    && apt-get install -y python3-pip \
     libsm6 \
     libxext6 \
     libxrender1 \
     libfontconfig1

# copy the requirements file into image
COPY ./requirements.txt /tmp/requirements.txt

# install requirements from file
RUN pip3 install -qr /tmp/requirements.txt

# add main program to /src/ directory
COPY main.py /src/

# set working directory to /src/
WORKDIR /src/

# invoke the main.py script upon container start
CMD ["python3", "main.py"]
