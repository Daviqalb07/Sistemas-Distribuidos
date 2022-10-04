import struct
import socket
import device_pb2
import messages_pb2

# 224 - 239
BUFFER_SIZE = 1024

class Device:
    def __init__(self, id: int, name: str, multicast_ip: str, multicast_port: int, sensor, actuator) -> None:
        self.id = id
        self.name = name
        self.multicast_ip = multicast_ip
        self.multicast_port = multicast_port
        self.sensor = sensor
        self.actuator = actuator

        server_ip, server_port = self.get_gateway_address()
        self.connect_to_gateway(server_ip, server_port)

    def get_gateway_address(self):
        self.sock_multicast = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock_multicast.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock_multicast.bind(('', self.multicast_port))

        m = struct.pack("4sl", socket.inet_aton(self.multicast_ip), socket.INADDR_ANY)
        self.sock_multicast.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, m)

        # server_ip, server_port = self.sock.recv(BUFFER_SIZE)
        # return server_ip, server_port
        return 'localhost', 8181

    def connect_to_gateway(self, server_ip, server_port):
        self.sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        message_join = messages_pb2.Request()
        message_join.type = "join"
        message_join.name = self.name

        message_join.sensor.id = self.id
        message_join.sensor.name = self.sensor.name
        message_join.sensor.value = self.sensor.value

        message_join.actuator.id = self.id
        message_join.actuator.name = self.actuator.name
        message_join.actuator.state = self.actuator.state

        # message_join.ip = self.multicast_ip
        # message_join.port = self.multicast_port

        self.sock_tcp.connect((server_ip, server_port))
        self.sock_tcp.send(message_join.SerializeToString())
        while True:
            pass