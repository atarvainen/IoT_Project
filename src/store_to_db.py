import re
import json
import pymysql
from peewee import *

# Unpack JSON object, modify mac address to int and call storeToDB for database handling
def sensor_Data_Handler(Topic, jsonData):
        obj = jsonData[1]
        accx = obj["acceleration_x"]
        accy = obj["acceleration_y"]
        accz = obj["acceleration_z"]
        hum = obj['humidity']
        power = obj["battery"]
        pres = obj["pressure"]
        temp = obj["temperature"]
        machex = jsonData[0]
        machexint = machex.split(":")
        macjoin = "".join(machexint)
        mac = int(macjoin, 16)
        machex = hex(mac)
        machex = re.findall("..", machex)
        machex.pop(0)
        machex = ":".join(machex)
        storeToDB(accx,accy,accz,hum,power,pres,temp,mac)

database = MySQLDatabase('iot', **{'password': '12345', 'charset': 'utf8', 'use_unicode': True, 'user': 'root'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Ruuvitag(BaseModel):
    ruuvitagid = BigAutoField(column_name='RuuviTagId')
    user = CharField(column_name='User', null=True)

    class Meta:
        table_name = 'RuuviTag'

class Data(BaseModel):
    acceleration_x = IntegerField(column_name='Acceleration-X', null=True)
    acceleration_y = IntegerField(column_name='Acceleration-Y', null=True)
    acceleration_z = IntegerField(column_name='Acceleration-Z', null=True)
    count = AutoField(column_name='Count')
    humidity = IntegerField(column_name='Humidity', null=True)
    power = IntegerField(column_name='Power', null=True)
    pressure = IntegerField(column_name='Pressure', null=True)
    ruuvitagid = ForeignKeyField(column_name='RuuviTagId', field='ruuvitagid', model=Ruuvitag)
    temp = IntegerField(column_name='Temp', null=True)
    time = DateTimeField(column_name='Time', null=True)

    class Meta:
        table_name = 'Data'

# Store data to db using Peewees imported class
def storeToDB(accx,accy,accz,hum,power,pres,temp,mac):
        print(accx,accy,accz,hum,power,pres,temp,mac)
        database.connect()
        DataToDb = Data.create(acceleration_x = accx,
acceleration_y=accy,
acceleration_z=accz,
humidity=hum,
power=power,
pressure=pres,
ruuvitagid=mac,
temp=temp)

        database.close()
