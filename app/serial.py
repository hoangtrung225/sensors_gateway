import serial

class Serial():
    DEFAULT_INTERFACE = '/dev/ttyUSB0'
    DEFAULT_BAUD = 115200

    def __init__(self, interface=DEFAULT_INTERFACE, baudrate=DEFAULT_BAUD):
        self.interface = interface
        self.baudrate = baudrate

    def connect(self):
        try:
            self.connection = serial.Serial(
               port=self.interface,\
               baudrate=self.baudrate,\
               parity=serial.PARITY_NONE,\
               stopbits=serial.STOPBITS_ONE,\
               bytesize=serial.EIGHTBITS,\
               timeout=1)
        except Exception as e:
            print(e)
        return self

    def close(self):
        if self.connection:
            self.connection.close()

    def read(self):
        if self.connection:
            return self.connection.read_line()

    def write(self, string):
        if self.connection:
            self.connection.write(string)
