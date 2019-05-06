from app import app
from app.models import Sensor 
from flask import jsonify

@app.route('/api/sensor/update', methods=['GET'])
def sensor_update():

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
            'rssi': record['rssi'] \
            })
    return jsonify(sensor_data)

@app.route('/api/sensor/<int:node_id>/data', methods=['GET'])
def get_sensor_data(node_id):

    #query database get all record about sensor node
    records = Sensor.query.filter(Sensor.node_id == node_id)
    sensor_data = []
    for record in records:
        data = record.to_dict()
        sensor_data.append(data)

    return jsonify(sensor_data)
