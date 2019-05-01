from app import db
import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

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

    def __repr__(self):
        return 'Create time {}'.format(self.created_date)
    
