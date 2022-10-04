import socket
import sys
import threading
import message_pb2
from properties import *


devices = []
def main():
    try:
        server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    except:
        print("Não deu certo :(")
        sys.exit(1)

    try:
        server_tcp.bind((GATEWAY_ADDRESS, GATEWAY_PORT))
        print(f"Server on na porta {GATEWAY_PORT} ! :D")
    except:
        print(f"Porta {GATEWAY_PORT} ocupada, tente novamente!")
        sys.exit(1)

    threading.Thread(target= discovery_devices, args= [server_udp]).start()
    server_tcp.listen()
    while True:
        try:
            connection, _ = server_tcp.accept()
            threading.Thread(target= handle_connection, args=[connection]).start()
        #     data, _ = connection.recv(BUFFER_SIZE)
        #     message = message_pb2.Message()
        #     message.ParseFromString(data)
        #     print("cheguei 0")

        #     if message.type == "DEVICE_JOIN":
        #         devices.append(message.device)
        #         threading.Thread(target= thread_recv_from_device, args=[connection]).start()
        #         print("entrou 1")
        #     elif message.type == "CLIENT_CONNECTION":
        #         threading.Thread(target= thread_client, args= [connection]).start()
        #         print("entrou 2")
        except:
            break
        
def handle_connection(connection: socket.socket):
    try:
        message = message_pb2.Message()
        data = connection.recv(BUFFER_SIZE)
        message.ParseFromString(data)
        if message.type == "DEVICE_JOIN":
            threading.Thread(target= thread_recv_from_device, args=[connection]).start()
        elif message.type == "CLIENT_JOIN":
            threading.Thread(target= thread_client, args=[connection]).start()

    except Exception as e:
        print(e)

def discovery_devices(server_udp: socket.socket):
    server_udp.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    while True:
        server_udp.sendto(bytes(f"{GATEWAY_ADDRESS} {GATEWAY_PORT}", encoding='utf-8'), ("224.1.1.1", 5001))

def thread_recv_from_device(device: socket.socket):
    past = 20
    while True:
        try:
            message = message_pb2.Message()
            data = device.recv(BUFFER_SIZE)
            message.ParseFromString(data)
            
        except Exception as e:
            print(e)

def thread_client(client: socket.socket):
    while True:
        try:
            message = message_pb2.Message()
            data = client.recv(BUFFER_SIZE)
            message.ParseFromString(data)

            
        except Exception as e:
            print(e)

main()