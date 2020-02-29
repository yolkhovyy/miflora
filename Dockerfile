FROM python:3

RUN mkdir /miflora-mqtt
WORKDIR /miflora-mqtt
ADD . /miflora-mqtt/

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install cron
RUN pip3 install "git+https://github.com/open-homeautomation/miflora.git"
RUN pip3 install "git+https://github.com/yolkhovyy/miflora.git"

COPY miflora-cron /etc/cron.d/miflora
RUN chmod 0644 /etc/cron.d/miflora

CMD cron -f