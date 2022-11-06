import struct
import socket
import sys
import protobuf.message_pb2 as message_pb2

# 224 - 239
BUFFER_SIZE = 1024

class Device:
    def __init__(self, id: int, name: str, multicast_ip: str, multicast_port: int, atributo, actions) -> None:
        self.id = id
        self.name = name
        self.multicast_ip = multicast_ip
        self.multicast_port = multicast_port
        self.atributo = atributo
        self.actions = actions
        self.action_flags = [0 for i in range(len(actions))] # uma flag para sinalizar um KeyboarInterrupt
        self.on = True

        server_ip, server_port = self.get_gateway_address()
        self.connect_to_gateway(server_ip, server_port)

    def get_gateway_address(self):
        self.sock_multicast = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.sock_multicast.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock_multicast.bind(('', self.multicast_port))

        m = struct.pack("4sl", socket.inet_aton(self.multicast_ip), socket.INADDR_ANY)
        self.sock_multicast.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, m)

        server_ip, server_port = self.sock_multicast.recv(BUFFER_SIZE).decode('utf-8').split()
        
        return server_ip, int(server_port)

    def connect_to_gateway(self, server_ip, server_port):
        self.sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        message_join = message_pb2.Message(type= "DEVICE_JOIN")
        message_join.device.id = self.id
        message_join.device.name = self.name
        message_join.device.on = self.on
        message_join.device.atributo.name = self.atributo['name']
        message_join.device.atributo.value = self.atributo['value']

        for action in self.actions:
            act = message_join.device.actions.add()
            act.id = action['id']
            act.name = action['name']


        server_address = (server_ip, server_port)
        self.sock_tcp.connect(server_address)
        self.sock_tcp.send(message_join.SerializeToString())
    
    def handle_connection(self):
        while True:
            request = message_pb2.Message()
            data = self.sock_tcp.recv(BUFFER_SIZE)
            request.ParseFromString(data)

            if request.type == "POST":
                if request.request.name == "action":
                    id_action = request.request.idAction
                    if self.search_action(id_action):
                        self.action_flags[id_action] = True
            



    def search_action(self, id_action):
        for action in self.actions:
            if action['id'] == id_action:
                return True
            
        return False
    
    def response_update(self):
        message_update = message_pb2.Message(type= "UPDATE_DEVICE")
        message_update.device.id = self.id
        message_update.device.name = self.name
        message_update.device.on = self.on
        message_update.device.atributo.name = self.atributo['name']
        message_update.device.atributo.value = self.atributo['value']

        for action in self.actions:
            act = message_update.device.actions.add()
            act.id = action['id']
            act.name = action['name']
        
        self.sock_tcp.send(message_update.SerializeToString())