import threading
from Device import *

class Lampada(Device):
    def __init__(self, id: int, multicast_ip: str, multicast_port: int, atributo, actions) -> None:
        super().__init__(id, "Lampada", multicast_ip, multicast_port, atributo, actions)
    
    def do_it(self):
        if any(self.action_flags):
            if self.action_flags[0]:
                self.on = not self.on
                self.action_flags[0] = False
            
            self.response_update()

            
atributo = {
    'name': 'presenca',
    'value': 1
}
actions = []
actions.append({
    'id': 0,
    'name': 'acender/apagar'
})
device = Lampada(id=1, multicast_ip="224.1.1.1", multicast_port=5001, 
                atributo= atributo, actions = actions)

threading.Thread(target= device.handle_connection).start()

while True:
    device.do_it()