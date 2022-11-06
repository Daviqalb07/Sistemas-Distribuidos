import random
import threading
from time import sleep
from Device import *


class SensorTemp(Device):
    def __init__(self, id: int, multicast_ip: str, multicast_port: int, atributo, actions) -> None:
        super().__init__(id, "Sensor de Temperatura", multicast_ip, multicast_port, atributo, actions)
    
    
    def change_temp(self):
        while True:
            if self.on:    
                sleep(8)
                temp = int(random.uniform(15, 35))
                self.atributo['value'] = temp

                self.response_update()
        

    def do_it(self):
        if any(self.action_flags):
            if self.action_flags[0]:
                self.on = not self.on
                self.action_flags[0] = False
            
            self.response_update()


atributo = {
    'name': 'temperatura',
    'value': int(random.uniform(15,35))
}
actions = []
actions.append({
    'id': 0,
    'name': 'ligar/desligar'
})

device = SensorTemp(id=4, multicast_ip="224.1.1.1", multicast_port=5001, 
                atributo= atributo, actions = actions)

threading.Thread(target= device.handle_connection).start()
threading.Thread(target=device.change_temp).start()

while True:
    device.do_it()