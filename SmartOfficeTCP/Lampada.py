import pb2.lampada_pb2 as lampada_pb2

RED = 0
GREEN = 1
BLUE = 2

class Lampada():
    def __init__(self, on = True, color = RED, sensor = False):
        self.on = on
        self.color = color
        self.sensor = sensor

    def power_on_off(self) -> bool:
        self.on = not self.on
        return self.on
    

    def get_on(self) -> bool:
        return self.on
    
    def set_on(self, on):
        self.on = on

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
    
    def get_sensor(self):
        return self.sensor
    
    def set_sensor(self, presence):
        self.sensor = presence

    def SerializeToString(self) -> bytes:
        lamp_serial = lampada_pb2.Lampada()
        lamp_serial.on = self.on
        lamp_serial.color = self.color
        lamp_serial.sensor = self.sensor
        return lamp_serial.SerializeToString()
    
    def ParseFromString(self, serialized: bytes):
        lamp_serial = lampada_pb2.Lampada()
        lamp_serial.ParseFromString(serialized)
        self.on = lamp_serial.on
        self.color = lamp_serial.color
        self.sensor = lamp_serial.sensor

    def print_fancy(self):
        print(f'Status: {self.on}')
        print(f'Color: {self.color}')
        print(f'Sensor: {self.sensor}')
    
    
