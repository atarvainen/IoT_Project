# IoT_Project

## Members: Antti Tarvainen, Hannu Oksman, Pekka Sivusuo, Antti Kettunen. Saku Tupala

### Communication platforms

Slack viestitykseen ja yhteydenottoihin
GitHub materiaalin kokoamiseen, jakamiseen ja säilytykseen

## Kulunvalvontajärjestelmä

Luokkaan raspi ja jokaiselle ryhmän jäsenelle Ruuvitag, jota käyttämällä he kirjautuvat sisälle ja ulos. Mitataan aikaa paljonko on tietyssä tilassa. Kerätään Ruuvitagilta kaikki data talteen.

### Sensors

5x ruuvitag (temperature, air humidity, air pressure, acceleration)
1x Breadboard
xx Resistors, LEDs etc.

### Controllers

Raspberry Pi 3

### Virtual Machines

Nimi: it-relaamo.labranet.jamk.fi

OS: Ubuntu Server 16.04

Kuvaus: Palvelin tulee IOT-järjestelmän kurssia varten kulunvalvonnan 
lokipalvelimeksi

Admin-tunnarit: L4163@student.jamk.fi

Voimassaolo: heti - 17.12.2018

Ei toistaiseksi tarvetta päästä ulkoverkosta erikseen.

## Intitial plan of the gateways

Bluetooth (Ruuvitag to Rasp)
MQTT (Rasp to Virtual Machine)
HTTPS (REST, Visualisation)
