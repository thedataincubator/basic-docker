# pull from ubuntu18 base image
FROM ubuntu:18.04

# install python3 into system
RUN apt-get update && apt-get install -y python3

# run python command during build process
RUN python3 -c "print('hello world')"

# when container is launched, run differenth python command
CMD ["python3", "-c", "print('hello world again')"]
