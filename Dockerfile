FROM ubuntu:latest
LABEL Maintainer="Christos Alexiou <pcnoic@gmail.com>" 

RUN apt update -y && apt upgrade -y

RUN apt install -y -q build-essential python3-pip python3-dev
RUN pip3 install -U pip setuptools wheel
RUN pip3 install gunicorn uvloop httptools

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY rgeocode/ /app

EXPOSE 80

ENTRYPOINT /usr/local/bin/gunicorn \
    -b 0.0.0.0:80 \
    -w 4 \
    -k uvicorn.workers.UvicornWorker main:app \
    --chdir /app
