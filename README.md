# IoT_Project

For detailed information see .docx and .pptx. Python scripts are in /src. We did most of the work in RasPi and VM, so this repo doesn't have that many commits. A lot of the work went into configurations, reading documentation and problem-solving. For information about Laravel and React, which were not the focus of this project, see this [repo](https://github.com/atarvainen/reactIoTproject). 

### Team Members: [Hannu Oksman](https://student.labranet.jamk.fi/~L2912/) ([GitHub](https://github.com/szeretni)), [Antti Tarvainen](https://github.com/atarvainen), [Pekka Sivusuo](https://github.com/pekkaXsiv), [Antti Kettunen](https://github.com/A-haCodes), [Saku Tupala](https://github.com/SnakkeZz)

## Intitial plan

### Communication platforms

Slack for communicating
GitHub for source codes

## Access Control / Monitoring System

Raspberry Pi as a controller for Ruuvitag sensors which are used to logging in. Raspberry Pi feeds Ruuvitags' data and logging data.

### Sensors

5x ruuvitag (temperature, air humidity, air pressure, acceleration)
1x Breadboard
xx Resistors, LEDs etc.

### Controllers

Raspberry Pi 3

### Virtual Machines

Name: it-relaamo.labranet.jamk.fi

OS: Ubuntu Server 16.04

Description: The server serves IoT-järjestelmän toteutus -courses access control -assignment.

Email: L4163@student.jamk.fi

Validity: now - 17.12.2018

For now we don't need access to the external network.

## Gateways

Bluetooth (Ruuvitag to Rasp)
MQTT (Rasp to Virtual Machine)
HTTPS (REST, Visualisation)

## Ticketing System

GitHub's issues

## Expansions

Security Alarm - new sensors? Camera, ir-sensor, speaker. 
