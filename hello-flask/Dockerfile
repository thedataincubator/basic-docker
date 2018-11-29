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
