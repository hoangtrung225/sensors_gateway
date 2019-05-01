import sys, os

dirpath = os.getcwd()
print("current directory is : " + dirpath)
sys.path.append('{}/..'.format(dirpath))

from app import db
from app.models import Sensor
from app import dbcontrol
from random import randint

class TestData():
    def __init__(self):
        self.file = open("data_test.txt", 'r')

    def insert_test_data(self):
        line_array = self.file.readline().split()
        db_control = dbcontrol.SensorDB()

        print("[DEBUG]Insert data test to Database")
        while len(line_array) != 0:
            print("[DEBUG]length of list: {}".format(len(line_array)))
            db_control.from_list(line_array)   
            line_array = self.file.readline().split()

        return
    
    def insert_random(self):
        sensor_data = {}
        db_control = dbcontrol.SensorDB() 
        for field in db_control.dict_struct:
            if field == 'node_id':
                sensor_data.update({field: randint(0, 5)})  
            sensor_data.update({field: randint(0, 50000)})
    
        db_control.insert_data(sensor_data) 
        
        

        
if __name__ == '__main__':
    test = TestData()
    test.insert_test_data()
