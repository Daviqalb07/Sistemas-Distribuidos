from Device import *

sensor = {
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
device = Device(id=2, name= "tv", multicast_ip="224.1.1.1", multicast_port=5001, 
                sensor= sensor, actions = actions)
