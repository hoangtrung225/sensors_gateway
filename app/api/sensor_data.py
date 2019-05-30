from app import app
from app.models import Sensor 
from flask import jsonify

@app.route('/api/sensor/<int:node_id>/data', methods=['GET'])
def get_sensor_data(node_id):

    #query database get all record about sensor node
    records = Sensor.query.filter(Sensor.node_id == node_id)
    sensor_data = []
    for record in records:
        data = record.to_dict()
        sensor_data.append(data)

    return jsonify(sensor_data)


