from app import app
from app.models import Sensor 
from flask import jsonify
from flask import request

@app.route('/api/sensor/timeline/<int:node_id>/<view>', methods=['GET'])
def get_sensor_timeline(node_id, view):

    if not view in ['light1', 'light2', 'temperature', 'humidity']:
        return None
    query = request.args.get("query")
    reverse = False
    if query != None and query.isdigit():
        records = Sensor.query.filter(Sensor.node_id == node_id).order_by(Sensor.created_date.desc()).limit(query)
        reverse = True
    else:
        #query database get all record about sensor node
        records = Sensor.query.filter(Sensor.node_id == node_id)
    sensor_data = {"view": view, "sensor": node_id}
    timeline_data = []
    for record in records:
        data = record.to_dict()
        timeline_data.append({
                "time": data["sys_time"],
                "data": data.get(view)
            })
    if reverse == True:
        timeline_data.reverse()
    sensor_data.update({"data": timeline_data})

    return jsonify(sensor_data)
