from app import app
from app.models import Sensor 
from flask import jsonify
from app.sensor_ctl import SensorCtl
from flask import request

sensor_ctl = SensorCtl()


@app.route('/api/control/network/start', methods=['GET'])
def start_collect():
    sensor_ctl.collect = True
    sensor_ctl.thread_collect = sensor_ctl.collect_data()
    return ""

@app.route('/api/control/network/stop', methods=['GET'])
def stop_collects():
    sensor_ctl.collect = False
    sensor_ctl.stop_services()
    if sensor_ctl.thread_collect != None:
         sensor_ctl.thread_collect.join()
    return ""

@app.route('/api/control/network/blink', methods=['GET'])
def blink_network():
    sensor_ctl.blink_network()
    return ""

@app.route('/api/control/sensor', methods=['GET'])
def run_command():
    query = request.args.get("query")
    if query != "show_buffer":
         output = sensor_ctl.send_cmd(query + '\n')
    
    data = {
    	"cmd": query,
	"data": sensor_ctl.buffer.decode("utf-8"),
    }
    return jsonify(data)
