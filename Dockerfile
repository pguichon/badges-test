FROM ubuntu:16.04

MAINTAINER Sketchfab

RUN apt-get -y update --fix-missing
RUN apt-get -y install \
    python-pip \
    python \
    libpq-dev

WORKDIR /sketchfab
COPY src /sketchfab
RUN pip install -r requirements.txt
