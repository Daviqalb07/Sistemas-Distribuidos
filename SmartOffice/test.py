from Device import *

sensor = {
    'name': 'presenca',
    'value': 1
}
actions = []
actions.append({
    'id': 0,
    'name': 'apagar'
})
actions.append({
    'id': 1,
    'name': 'acender'
})
device = Device(id=1, name= "lampada", multicast_ip="224.1.1.1", multicast_port=5001, 
                sensor= sensor, actions = actions)
