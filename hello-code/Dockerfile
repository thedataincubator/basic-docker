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
