# From TTOS0100 GitLab

import paho.mqtt.client as mqtt
from ruuvitag_sensor.ruuvitag import RuuviTag
import time
import json
import random
# False = Ruuvitag mode
# True = Debug mode
DEBUG = True
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
# Function to calculate outside temperature 
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
		print("TEMP IN:", in_temp," TEMP OUT:", out_temp, " HUMIDY IN:",in_humidy," HUMIDY OUT:",out_humidy," \n")
		res = json.dumps(d)
		return res
	else:
		print("Ruuvitag MODE in use")
		sensor = RuuviTag(sensor_mac)
		data = sensor.update()
		src = str.format('Sensor - {0}', sensor_mac)
		temp = data['temperature']
		humidy = data['humidity']
		pressure = data['pressure']    
    
		d ={
			"mac": sensor_mac, 
			"temp": temp,
 			"humidy": humidy,
			"pressure": pressure	
    		}
		print("MAC:", sensor_mac," temperature:", temp, " humidy:",humidy," pressure:",pressure," \n")
		res = json.dumps(d)
		return res
if DEBUG:
	print("DEBUG MODE")
	macs =[]
else:
	# Define Ruuvitag MAC-address in mode:
	# macs = ['AA:BB:CC:DD:EE:FF','AB:CD:EF:BA:DC:FE:']
	macs = ['ADD MAC1','ADD MAC2']
	
# MQTT specifications STARTS here
#Topic of published message, DO NOT CHANGE
PUB_TOPIC_1="iot-2/evt/status/fmt/json"
#Tpic of subscribe message, DO NOT change
SUB_TOPIC_1="iot-2/cmd/update/fmt/json"
#Unique client ID, defined in Device section/Bluemix     
#client_id="d:org-ID:device-type:device-ID"
client_id="d:org-ID:device-type:device-ID"
#Address of Bluemix MQTT Broker
#Syntax: 
#broker="org-ID.messaging.internetofthings.ibmcloud.com"
broker="org-ID.messaging.internetofthings.ibmcloud.com"
#Define port: TCP=1883, TSL=8883
port=1883
#Time to keep connection alive (sec)
alive=60
#Authentication details
userid="use-token-auth"
#Add paasword
passwd="password"
#QoS settings
QoS0 = 0
QoS1 = 1
QoS2 = 2
# Create a MQTT client
client = mqtt.Client(client_id,True)
# Set authentication
client.username_pw_set(userid,passwd)
#Register callback to get debug information
client.on_connect = on_connect
client.on_publish = on_publish
#Connect to Watson IoT Platform
#client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect(broker,port,alive)
print("Subscribe send\n")
client.subscribe(SUB_TOPIC_1,QoS0)
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
                        for index in range(0,len(macs)):
                                msg=climate(macs[index])
                                (rc,mid) = client.publish(PUB_TOPIC_1,msg,QoS0,True)
                                time.sleep(10)
        except KeyboardInterrupt:
                break
print("Katkaistaan yhteys")
client.loop_stop()
client.unsubscribe(PUB_TOPIC_1)
client.disconnect()
