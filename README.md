# Docker Examples

These are three examples which demonstrate some of the features of Docker and containers in general!

## Why Docker?
Its awesome.  But additionally it solves several problems in reasonable (subjective I know) ways.  Docker helps manage *containers* a technology which leverages the OS kernels ability isolate system resources and processes.  This means instead of a single machine (or virtual machine, its a cloud world after all), to run each application to ensure the applications do not interfere, we can use containers to run several processes on the same host.  Its important to remember that containers however, are not VM's, they are more of a collection of isolated process than a true isolated system.  This means containers are more "lightweight" than VM's and have almost bare metal performance, but can have increased security concerns.

Docker does a few things with containers, but at the heart its an api for making it easy to create, distribute, and abstract containers (yes, layers of abstractions).  It differs from other containerization techniques in that it is meant to build an environment for running a single process, if you want multiple processes, use multiple Docker containers.  There are ways to get around this sort of philosophy especially when it does odd things (see [dumb-init](https://github.com/Yelp/dumb-init)), but for most part it works just fine.  Now you might ask, "How do I coordinate a bunch of different processes if they are all in different Docker containers and need to communicate and what not?"  This is why we have things like Kubernetes and more generally container-orchestration.

## How to Docker

Now to the basics, the main "things" in Docker are images and containers (you might argue a container is not a thing, I don't disagree hence the quotes).  Think of the image as a description of an entire operating system with all the libraries and code needed to run a particular application.  The container can be thought of as an instance of that image.  Thus, given a Docker image I can spin up identical containers on different machine.  Thus using Docker is simply creating the proper Docker image and then launching containers from it when necessary.  So first we need to learn how to create the images.  This is where the Dockerfile comes in handy.

### The Dockerfile

The Dockerfile is the description for how an image is built, they are not exactly one to one (the image built from a Dockerfile today might be different than the one built from the same Dockerfile tomorrow), but it is a good description of the image.  The Dockerfile describes taking a base image (usually something like a very basic operating system) and performing a set of operations on that image.  These operations are kind of like git commits and they form layers on the image.  Some common commands are

- **COPY** - copy a file from local filesystem into image
- **RUN** - run a command in the image
- **FROM** - use a base image
- **ENV** - set environments

Every time a command is run, Docker effectively creates a container from the previous layers, runs the command inside the container and then commits the state.  Thus a Dockerfile is kind of like a master bash script running on a bare starting operating system.

One nice thing about Docker is that it provides cacheing of the layers, so if only a later layer is altered, the previous layers don't need to be rebuilt.  We will see some examples of Dockerfiles in just a bit, but first we need to know how to tell Docker to actually do something with them.

## Docker client

The Docker client has a ton of functionality, but for the basics we really only need to know a few commands

- **docker build** - build image for dockerfile
- **docker run** - create container from image
- **docker exec** - go into a running container
- **docker images** - manage images on system

Lets see a few different examples and walk through some tricky bits.

## Examples

## hello-world
This is the most basic example.  This builds an image from a base of Ubuntu 18 and installs Python 3.  It then uses **RUN** to print something with Python as well as **CMD** to print out a similiar thing.  The difference is that the **RUN** command executes during the build process, whereas the **CMD** executes when the container is launched.  To build this container run from the `hello-world` directory `docker build -t hello-world .`.  The `-t` flag gives the container a tag and the `.` tells the engine to use the current directory as the Docker context.  Docker will only allow you to use files and resources from within the current context.  To run the container you can use `docker run -i hello-world`, the `-i` flag will allow you to see the output.
```dockerfile
# pull from ubuntu18 base image
FROM ubuntu:18.04

# install python3 into system
RUN apt-get update && apt-get install -y python3

# run python command during build process
RUN python3 -c "print('hello world')"

# when container is launched, run differenth python command
CMD ["python3", "-c", "print('hello world again')"]

```

Once you run this once, try building it again.  Does it still give both outputs?
## hello-code
```dockerfile
FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y python3-pip \
     libsm6 \
     libxext6 \
     libxrender1 \
     libfontconfig1

COPY ./requirements.txt /tmp/requirements.txt

RUN pip3 install -qr /tmp/requirements.txt

COPY main.py /src/

WORKDIR /src/

CMD ["python3", "main.py"]

```
## hello-flask
```dockerfile
FROM alpine:edge

RUN apk update && apk add --no-cache \
    python3 \
    py3-psycopg2 && \
    python3 -m ensurepip

ADD ./app/requirements.txt /tmp/requirements.txt

RUN pip3 install -qr /tmp/requirements.txt

COPY ./app /opt/app/

WORKDIR /opt/app

CMD gunicorn --bind 0.0.0.0:$PORT wsgi

```
