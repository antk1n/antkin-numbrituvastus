FROM ubuntu:16.04

ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir -p /var/www
WORKDIR /var/www

RUN apt-get update

RUN apt-get install -y openalpr openalpr-daemon openalpr-utils libopenalpr-dev

WORKDIR /var/www/
