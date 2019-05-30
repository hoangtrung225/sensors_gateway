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
            'rssi': record['rssi'], \
            'timestamp': record['sys_time']
            })
    return jsonify(sensor_data)


