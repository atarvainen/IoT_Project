'''
Print sensor data to the screen. Update interval 2 sec.

Press Ctrl+C to quit.

2017-02-02 13:45:25.233400
Sensor - F4:A5:74:89:16:57
Temperature: 10
Humidity:    28
Pressure:    689
'''

import time
import os
from datetime import datetime

from ruuvitag_sensor.ruuvitag import RuuviTag

# Change here your own device's mac-address
mac = 'E7:78:E4:6B:A3:31'
mac1 = 'D1:F1:8D:F9:64:51'

print('Starting')

sensor = RuuviTag(mac)
sensor1 = RuuviTag(mac1)

while True:
    data = sensor.update()
    data1 = sensor1.update()

    line_sen = str.format('Sensor - {0}', mac)
    line_tem = str.format('Temperature: {0} C', data['temperature'])
    line_hum = str.format('Humidity:    {0}', data['humidity'])
    line_pre = str.format('Pressure:    {0}', data['pressure'])
    line_x = str.format('X-axis:    {0}', data['acceleration_x'])
    line_y = str.format('Y-axis:    {0}', data['acceleration_y'])
    line_z = str.format('z-axis:    {0}', data['acceleration_z'])

    # Clear screen and print sensor data
    os.system('clear')
    print('Press Ctrl+C to quit.\n\r\n\r')
    print(str(datetime.now()))
    print(line_sen)
    print(line_tem)
    print(line_hum)
    print(line_pre)
    print(line_x)
    print(line_y)
    print(line_z)
    
    line_sen = str.format('Sensor - {0}', mac1)
    line_tem = str.format('Temperature: {0} C', data1['temperature'])
    line_hum = str.format('Humidity:    {0}', data1['humidity'])
    line_pre = str.format('Pressure:    {0}', data1['pressure'])
   # line_x = str.format('X-axis:    {0}', data1['acceleration_x'])
   # line_y = str.format('Y-axis:    {0}', data1['acceleration_y'])
   # line_z = str.format('z-axis:    {0}', data1['acceleration_z'])

    print("\n"+line_sen)
    print(line_tem)
    print(line_hum)
    print(line_pre)
   # print(line_x)
   # print(line_y)
   # print(line_z)
    print('\n\r\n\r.......')

    # Wait for 2 seconds and start over again
    try:
        time.sleep(2)
    except KeyboardInterrupt:
        # When Ctrl+C is pressed execution of the while loop is stopped
        print('Exit')
        break