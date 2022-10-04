import struct
import socket
import message_pb2
from properties import BUFFER_SIZE
# 224 - 239


class Device:
    def __init__(self, id: int, name: str, multicast_ip: str, multicast_port: int, sensor, actions) -> None:
        self.id = id
        self.name = name
        self.multicast_ip = multicast_ip
        self.multicast_port = multicast_port
        self.sensor = sensor
        self.actions = actions

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

        message_join = message_pb2.Message()
        message_join.type = "DEVICE_JOIN"

        message_join.device.name = self.name
        message_join.device.sensor.name = self.sensor['name']
        message_join.device.sensor.value = self.sensor['value']

        for action in self.actions:
            act = message_join.device.actions.add()
            act.id = action['id']
            act.name = action['name']
        # message_join.ip = self.multicast_ip
        # message_join.port = self.multicast_port

        server_address = (server_ip, server_port)
        self.sock_tcp.connect(server_address)
        self.sock_tcp.send(message_join.SerializeToString())