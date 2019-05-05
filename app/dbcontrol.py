from app.models import Sensor
from app import db
 
class SensorDB():
    """gateway controller to push sensor data to sqlite"""
    dict_struct = \
    [
        "data_len" ,
        "timestamp1" ,
        "timestamp2" ,
        "timesynctimestamp" ,
        "node_id" ,
        "seqno" ,
        "hops" ,
        "latency" ,
        "data_len2" ,
        "clock" ,
        "timesynchtime" ,
        "time_cpu" ,
        "time_lpm" ,
        "time_transmit" ,
        "time_listen" ,
        "best_neighbor" ,
        "best_neighbor_etx" ,
        "rtmetric" ,
        "num_neighbors" ,
        "beacon_interval" ,
        "battery_voltage" ,
        "battery_indicator" ,
        "light1" ,
        "light2" ,
        "temperature" ,
        "humidity" ,
        "rssi" 
    ]
    def __init__(self):
        return

    @staticmethod
    def insert_data(data):
        """Insert dict sensor object to database"""
        print("[DEBUG]Insert to database sensor info {}".format(data['node_id'])) 
        sensor = Sensor()
        for field in SensorDB.dict_struct:
            if field in data:
                setattr(sensor, field, data[field])
        
        try:
            db.session.add(sensor)
            db.session.commit()
        except Exception as e:
            print("Error: {}".format(e))
       
        return sensor

    @staticmethod
    def list_to_dict(l):
        sensor = {}
        counter = 0
        for field in SensorDB.dict_struct:
            sensor.update({field: l[counter]})
            counter += 1

        return sensor
    
    @staticmethod
    def from_list(l):
        d = SensorDB.list_to_dict(l)
        SensorDB.insert_data(d)
