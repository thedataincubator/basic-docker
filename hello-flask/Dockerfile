# use apline base image
FROM alpine:edge

# install os dependencies
RUN apk update && apk add --no-cache \
    python3 \
    py3-psycopg2 && \
    python3 -m ensurepip

# copy over requirements
COPY ./app/requirements.txt /tmp/requirements.txt

# install requirements
RUN pip3 install -qr /tmp/requirements.txt

# copy application
COPY ./app /opt/app/

# set working directory
WORKDIR /opt/app

# launch server
CMD gunicorn --bind 0.0.0.0:$PORT wsgi
