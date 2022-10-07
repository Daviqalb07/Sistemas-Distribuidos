import threading
from Device import *

class Tv(Device):
    def __init__(self, id: int, multicast_ip: str, multicast_port: int, atributo, actions) -> None:
        super().__init__(id, "tv", multicast_ip, multicast_port, atributo, actions)
    
    def do_it(self):
        if any(self.action_flags):
            if self.action_flags[0]:
                self.atributo['value'] += 1
                self.action_flags[0] = False
            if self.action_flags[1]:
                self.atributo['value'] -= 1
                self.action_flags[1] = False
            if self.action_flags[2]:
                self.on = True
                self.action_flags[2] = False
            if self.action_flags[3]:
                self.on = False
                self.action_flags[3] = False
            
            self.response_update()


atributo = {
    'name': 'volume',
    'value': 50
}
actions = []
actions.append({
    'id': 0,
    'name': 'aumentar'
})
actions.append({
    'id': 1,
    'name': 'diminuir'
})
actions.append({
    'id': 2,
    'name': 'ligar'
})
actions.append({
    'id': 3,
    'name': 'desligar'
})
device = Tv(id=2, multicast_ip="224.1.1.1", multicast_port=5001, 
                atributo= atributo, actions = actions)

threading.Thread(target= device.handle_connection).start()

while True:
    device.do_it()