import os, sys
dirpath = os.getcwd()
print("current directory is : " + dirpath)
sys.path.append('{}/..'.format(dirpath))

import serial
from app.models import Sensor
from app import dbcontrol, db
import threading
import time

class SensorCtl():

    DEFAULT_INTERFACE = '/dev/ttyUSB0'
    DEFAULT_BAUD = 115200

    def __init__(self, interface=DEFAULT_INTERFACE, baudrate=DEFAULT_BAUD):
        self.sensor_ctl = serial.Serial(
               port=interface,\
               baudrate=baudrate,\
               parity=serial.PARITY_NONE,\
               stopbits=serial.STOPBITS_ONE,\
               bytesize=serial.EIGHTBITS,\
               timeout=1)
        self.wait_cmd = False
        self.lock = threading.Semaphore()
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
        
        #send collect command to network
        self.sensor_ctl.write(str.encode("collect | timestamp | binprint &\n"))
        #self.sensor_ctl.write(str.encode("repeat 0 60 { randwait 60 collect-view-data | send 31 }\n"))
        self.sensor_ctl.write(str.encode("netcmd { repeat 0 20 { randwait 20 collect-view-data | blink | send } }\n"))

        #run forever read data from serial interface push to database 
        while True:
            self.lock.acquire()
            if not self.wait_cmd:
                print("[DEBUG]inside while loop")
                sensor_data = self.sensor_ctl.readline().split()
                print("[DEBUG] {}".format(sensor_data))
                if len(sensor_data) == 30:
                    print("[DEBUG]Insert sensor data to Database")
                    dbcontrol.SensorDB.from_list(sensor_data)   
            self.lock.release()
            time.sleep(1)

    @threaded
    def send_cmd(self, cmd):
        #send command wait to read response and return
        self.lock.acquire()
        self.wait_cmd = True
        self.sensor_ctl.write(cmd)
        data = self.sensor_ctl.read_until(b"Contiki>\r\n")
        print("read data: {}".format(data))
        self.wait_cmd = False
        self.lock.release()
        return data
    
    def run(self):
        collect_thread = self.collect_data()

if __name__ == '__main__':
    ctl = SensorCtl()
    ctl.run()
    # count = 0
    # print("[DEBUG]inside main")
    # while True:
    #     ctl.send_cmd(str.encode("netcmd {blink 1}\n"))
    #     print("[DEBUG]Inside thread {}".format(count))
    #     count+=count
    #     time.sleep(5)
