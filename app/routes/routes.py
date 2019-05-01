from app import app
from flask import render_template
from app.models import Sensor

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.htm')

@app.route('/sensor')
def sensor_info():

    #query database get newest record for sensors
    records = Sensor.query.group_by('node_id')
    sensor_data = []
    for record in records:
        sensor_data.append({
            'node_id':  record.node_id, \
            'battery_voltage':  record.battery_voltage, \
            'light1':   record.light1, \
            'light2':   record.light2, \
            'temperature':  record.temperature, \
            'humidity': record.humidity, \
            'rssi': record.rssi \
            })
    print("[DEBUG]sensors data: {}".format(sensor_data))
    return render_template('sensor.htm', sensors=sensor_data)
