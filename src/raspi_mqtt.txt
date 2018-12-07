#!/usr/bin/env python3

import paho.mqtt.client as mqtt
from ruuvitag_sensor.ruuvitag import RuuviTag
from ruuvitag_sensor.ruuvi import RuuviTagSensor
import time
import json
import random

# False = Ruuvitag mode
# True = Debug mode
DEBUG = False
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #  client.subscribe(PUB_TOPIC_1)
def on_subscribe(client,userdata,mid,granted_qos):
    print("Subsribed: "+srt(mid)+" "+str(granted_qos))
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
def handle_data(data):
#    print('MAC ' + data[0])
#    print(data[1])
    time.sleep(5)

    '''
    temp = data['temperature']
    humidy = data['humidity']
    pressure = data['pressure']
    acceleration_x = data['acceleration_x']
    acceleration_y = data['acceleration_y']
    acceleration_z = data['acceleration_z']
    battery = data['battery']
    d ={
        "mac": sensor_mac,
        "temp": temp,
        "humidy": humidy,
        "pressure": pressure,
        "acceleration_x" : acceleration_x,
        "acceleration_y" : acceleration_y,
        "acceleration_z" : acceleration_z,
        "power" : battery
    }
    print("MAC:", sensor_mac," temperature:", temp, " humidity:",humidy," pressu                                                      re:",pressure," acceleration_x:",acceleration_x," acceleration_y:"," acceleratio                                                      n_z:",acceleration_z," power:",battery," \n")
    '''

    res = json.dumps(data)
    print(res)
    (rc,mid) = client.publish(PUB_TOPIC_1,res,QoS0,True)

'''
def climate(sensor_mac):
    if DEBUG:
        print("DEBUG version in use")
        in_temp = round(random.uniform(19.5,22.0),1)
        in_humidy = random.randint(20,30)
        out_temp = round(random.uniform(10.0,15.0),1)
        out_humidy = random.randint(50,80)
        d ={
            "temp_in": in_temp,
            "humidy_in": in_humidy,
            "temp_out": out_temp,
            "humidy_out": out_humidy,
        }
        print("TEMP IN:", in_temp," TEMP OUT:", out_temp, " HUMIDY IN:",in_humid                                                      y," HUMIDY OUT:",out_humidy," \n")
        res = json.dumps(d)
        return res
    else:
        RuuviTagSensor.get_datas(handle_data,sensor_mac)
'''

if DEBUG:
        print("DEBUG MODE")
        macs =[]
else:
        #Define Ruuvitag MAC-address in mode:
        macs = ['EA:17:44:5F:8E:80','D4:4E:CF:67:7B:67','DE:2E:3D:B4:6F:6E','C1:                                                      34:47:15:0E:3B','D1:7D:78:B0:FC:54']

# MQTT specifications STARTS here
#Topic of published message, DO NOT CHANGE
PUB_TOPIC_1="iot-2/evt/status/fmt/json"
#Tpic of subscribe message, DO NOT change
SUB_TOPIC_1="iot-2/cmd/update/fmt/json"
#Unique client ID, defined in Device section/Bluemix
#client_id="d:org-ID:device-type:device-ID"
client_id="clientId"
#Address of Bluemix MQTT Broker
#Syntax:
#broker="org-ID.messaging.internetofthings.ibmcloud.com"
broker="192.168.54.101"
#Define port: TCP=1883, TSL=8883
port=1883
#Time to keep connection alive (sec)
alive=60
#Authentication details
userid="iotProject"
#Add password
passwd="systemctlusage"
#QoS settings
QoS0 = 0
QoS1 = 1
QoS2 = 2
# Create a MQTT client
client = mqtt.Client(client_id,True)
#client.disconnect()
# Set authentication
client.username_pw_set(userid,passwd)
#Register callback to get debug information
client.on_connect = on_connect
client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect(broker,port,alive)
#print("Subscribe send\n")
#client.subscribe(SUB_TOPIC_1,QoS0)
print("Start listening")
client.loop_start()
#Send data to broker
print("Start to Publish messages")
while True:
        try:
                if DEBUG:
                        msg=climate(macs)
                        (rc,mid) = client.publish(PUB_TOPIC_1,msg,QoS0,True)
                        time.sleep(30)
                else:
                        print("Sending")
                        RuuviTagSensor.get_datas(handle_data,macs)
        except KeyboardInterrupt:
           break
        except Exception as e:
           print(e.args)
print("Katkaistaan yhteys")
client.loop_stop()
client.unsubscribe(PUB_TOPIC_1)
client.disconnect()
