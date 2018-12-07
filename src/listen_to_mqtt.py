#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import json
from BAstore import sensor_Data_Handler
# MQTT Settings
MQTT_Username = "iotProject"
MQTT_Password = "systemctlusage"

#Save Data into DB Table
def on_message(mosq, obj, msg):
        # This is the Master Call for saving MQTT Data into DB
        # For details of "sensor_Data_Handler" function please refer "sensor_dat                                                      a_to_db.py"
        print("MQTT Data Received...")
        print("MQTT Topic: " + msg.topic)
        encoded = json.loads(msg.payload)
        print("encoded payload @ BAlisten:")
        print(encoded)
        sensor_Data_Handler(msg.topic, encoded)

# Subscribe to client on connect so we automatically resubscribe after reconnecting
def on_connect(client, userdta, flags, rc):
		#Subscribe to all Sensors at Base Topic
        client.subscribe("iot-2/evt/status/fmt/#", 0)

mqttc = mqtt.Client()

# Set username and password as a set
mqttc.username_pw_set(MQTT_Username,MQTT_Password)

# Assign event callbacks
mqttc.on_message = on_message

# Connect
mqttc.connect("192.168.54.101", 1883, 60)

# Call on_connect when connected
mqttc.on_connect = on_connect

# Continue the network loop
mqttc.loop_forever(retry_first_connection=True)
