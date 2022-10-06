from Device import *

sensor = {
    'name': 'temperatura',
    'value': 24
}
actions = []
actions.append({
    'id': 0,
    'name': 'aumentar 1ºC'
})
actions.append({
    'id': 1,
    'name': 'diminuir 1ºC'
})
actions.append({
    'id': 2,
    'name': 'ligar'
})
actions.append({
    'id': 3,
    'name': 'desligar'
})
device = Device(id=3, name= "Ar Condicionado", multicast_ip="224.1.1.1", multicast_port=5001, 
                sensor= sensor, actions = actions)
