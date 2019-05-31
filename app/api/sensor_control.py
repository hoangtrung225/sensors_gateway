from app import app
from app.models import Sensor 
from flask import jsonify
from app.sensor_ctl import SensorCtl

sensor_ctl = SensorCtl()


@app.route('/api/control/network/start', methods=['GET'])
def start_collect():
    sensor_ctl.collect_data()
    return ""

@app.route('/api/control/network/stop', methods=['GET'])
def stop_collects():
    sensor_ctl.stop_services()
    return ""

@app.route('/api/control/network/blink', methods=['GET'])
def blink_network():
    sensor_ctl.blink_network()
    return ""
