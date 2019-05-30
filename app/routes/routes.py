from app import app
from flask import render_template
from app.models import Sensor
from app.sys_info import SystemInfo
import time

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    system_info = SystemInfo()
    network = system_info.network_info()
    system = system_info.system_info()
    processes = system_info.system_process()
    return render_template('index.htm', network=network, system=system, processes=processes)

@app.route('/sensor')
def sensor_info():

    #query database get newest record for sensors
    records = Sensor.query.group_by('node_id')
    sensor_data = []
    for record in records:
        record = record.to_dict()
        sensor_data.append({
            'node_id':  record['node_id'], \
            'battery_voltage':  record['battery_voltage'], \
            'light1':   record['light1'], \
            'light2':   record['light2'], \
            'temperature':  record['temperature'], \
            'humidity': record['humidity'], \
            'rssi': record['rssi'], \
            'timestamp': record['sys_time'].strftime("%z %a %b %d %Y %H:%M:%S")
            })
    print("[DEBUG]sensors data: {}".format(sensor_data))
    return render_template('sensor.htm', sensors=sensor_data)

@app.route('/timeline')
def sensor_timeline():
    
    records = Sensor.query.group_by('node_id')
    sensors = []
    for record in records:
        sensors.append(record.node_id)
    
    view_options = ['light1', 'light2', 'temperature', 'humidity']
    return render_template('timeline.htm', sensors=sensors, views=view_options)
