import os, sys
dirpath = os.getcwd()
print("current directory is : " + dirpath)
sys.path.append('{}/.'.format(dirpath))

from app.serial import Serial
from app.models import Sensor
from app import dbcontrol, db
import threading
import time

class SensorCtl():
    
    def __init__(self):
        self.sensor_ctl = Serial().connect()
        if not self.sensor_ctl:
            raise Exception("[ERROR]: Fail to connect to serial interface")
        self.wait_cmd = False
        self.db_control = dbcontrol.SensorDB()
        self.threads = []

    def threaded(fn):
        """define thread wraper function"""
        def wrapper(*args, **kwargs):
            thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
            thread.start()
            return thread
        return wrapper
    
    @threaded
    def collect_data(self):
       #run forever read data from serial interface push to database

       while True:
            if not self.wait_cmd:
                sensor_data = self.sensor_ctl.read().split()
                if len(sensor_data):
                    print("[DEBUG]Insert sensor data to Database")
                    db_control.from_list(sensor_data)   
            
            time.sleep(5)

    @threaded
    def send_cmd(self, cmd):
        #send command wait to read response and return

        self.wait_cmd = True
        self.sensor_ctl.write(cmd)
        data = self.sensor_ctl.read()
        self.wait_cmd = False

        return data
    
    def run(self):
        collect_thread = self.collect_data()
        collect_thread.join() 

if __name__ == '__main__':
    ctl = SensorCtl()
    ctl.run()
    count = 0
    while True:
        ctl.send_cmd("hello")
        print("[DEBUG]Inside thread {}".format(++count))
        time.sleep(5)
