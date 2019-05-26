from app import db
import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    privilege = db.Column(db.Integer)

    USER = 1
    ADMIN = 2
    BACKEND_SERVER = 3

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Sensor(db.Model):
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, primary_key=True)
    data_len = db.Column(db.Integer)
    timestamp1 = db.Column(db.Integer)
    timestamp2 = db.Column(db.Integer)
    timesynctimestamp = db.Column(db.Integer)
    node_id = db.Column(db.Integer)
    seqno = db.Column(db.Integer)
    hops = db.Column(db.Integer)
    latency = db.Column(db.Integer)
    data_len2 = db.Column(db.Integer)
    clock = db.Column(db.Integer)
    timesynchtime = db.Column(db.Integer)
    time_cpu = db.Column(db.Integer)
    time_lpm = db.Column(db.Integer)
    time_transmit = db.Column(db.Integer)
    time_listen = db.Column(db.Integer)
    best_neighbor = db.Column(db.Integer)
    best_neighbor_etx = db.Column(db.Integer)
    rtmetric = db.Column(db.Integer)
    num_neighbors = db.Column(db.Integer)
    beacon_interval = db.Column(db.Integer)
    battery_voltage = db.Column(db.Integer)
    battery_indicator = db.Column(db.Integer)
    light1 = db.Column(db.Integer)
    light2 = db.Column(db.Integer)
    temperature = db.Column(db.Integer)
    humidity = db.Column(db.Integer)
    rssi = db.Column(db.Integer)

    TICKS_PER_SECOND= 4096
    VOLTAGE= 3
    POWER_CPU= 1.800 * VOLTAGE;       
    POWER_LPM= 0.0545 * VOLTAGE;      
    POWER_TRANSMIT= 17.7 * VOLTAGE;   
    POWER_LISTEN= 20.0 * VOLTAGE;     


    def __repr__(self):
        return 'Create time {}'.format(self.created_date)
    
    def to_dict(self):
        data = {
            'node_id': self.node_id,
            'battery_voltage' : self.battery_voltage * 2 * 2.5 / 4096.0,
            'light1': 10.0 * self.light1 / 7.0,
            'light2': 46.0 * self.light2 / 7.0,
            'temperature': -39.6 + 0.01 * self.temperature,
            'humidity': -4.0 + 405.0 * self.humidity / 10000,
            'latency': self.latency / 32678.0,
            'rssi': self.rssi,
            'best_neighbor': self.best_neighbor if self.best_neighbor > 0 else None,
            'best_neighbor_etx': self.best_neighbor_etx / 8.0,
            'cpu_power': (self.time_cpu * self.POWER_CPU) / (self.time_cpu + self.time_lpm),
            'lpm_power': (self.time_lpm * self.POWER_LPM) / (self.time_cpu + self.time_lpm),
            'listen_power': (self.time_listen * self.POWER_LISTEN) / (self.time_cpu + self.time_lpm),
            'tranx_power': (self.time_transmit * self.POWER_TRANSMIT) / (self.time_cpu* self.time_lpm),
            'average_power': (self.time_cpu * self.POWER_CPU + self.time_lpm * \
                    self.POWER_LPM + self.time_listen * self.POWER_LISTEN +\
                    self.time_transmit * self.POWER_TRANSMIT) / (self.time_cpu + self.time_lpm),
            'power_time': 1000 * (self.time_cpu + self.time_lpm) / self.TICKS_PER_SECOND,
            'sys_time': self.created_date,
            'node_time': ((self.timestamp1 << 16) + self.timestamp2) * 1000
        }

        return data
