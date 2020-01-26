# Simple MQTT bridge for Xiaomi Mi Flora plant sensor

This application lets you read sensor data from a Xiaomi Mi Flora plant sensor.

## Functionality 
It supports reading the different measurements from the sensor
- temperature
- moisture
- conductivity
- brightness

To use this application you will need a Bluetooth Low Energy dongle attached to your computer. You will also need a Xiaomi Mi Flora plant sensor. 

## Dependecies
This application depends on the 
https://github.com/open-homeautomation/miflora.git
library.

Library installation:
```bash
$ pip3 install git+https://github.com/open-homeautomation/miflora.git
```

## crontab
```
*/15 * * * * python3 /home/pi/miflora/miflora-mqtt.py C4:7C:8D:xx:xx:xx -m -e -s mqtt-server
```