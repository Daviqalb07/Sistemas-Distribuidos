import socket
import sys
import threading
import devices.protobuf.message_pb2 as message_pb2 
from properties import *


devices = []
clients = []


def main():
    try:
        server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    except Exception as e:
        print(e)
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
        
        except:
            break



def discovery_devices(server_udp: socket.socket):
    server_udp.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    while True:
        server_udp.sendto(bytes(f"{GATEWAY_ADDRESS} {GATEWAY_PORT}", encoding='utf-8'), ("224.1.1.1", 5001))



def handle_connection(connection: socket.socket):
    try:
        message = message_pb2.Message()
        data = connection.recv(BUFFER_SIZE)
        message.ParseFromString(data)
        
        if message.type == "DEVICE_JOIN":
            update_device(message, connection, CREATE_DEVICE)
            threading.Thread(target= thread_recv_from_device, args=[connection, len(devices)-1]).start()
        elif message.type == "CLIENT_JOIN":
            clients.append(connection)
            threading.Thread(target= thread_client, args=[connection]).start()

    except Exception as e:
        print(e)



def thread_recv_from_device(device: socket.socket, index_device):
    global devices
    while True:
        try:
            message = message_pb2.Message()
            data = device.recv(BUFFER_SIZE)
            message.ParseFromString(data)
            
            if message.type == "UPDATE_DEVICE":
                update_device(message, device, index_device)
                print(f"len(devices) = {len(devices)}")
            elif message.type == "REMOVE_DEVICE":
                devices.pop(index_device)
                print(f"len(devices) = {len(devices)}")
        except Exception as e:
            print(e)



def thread_client(client: socket.socket):
    global devices

    while True:
        try:
            message = message_pb2.Message()
            data = client.recv(BUFFER_SIZE)
            message.ParseFromString(data)

            if message.type == "GET":
                if message.request.name == "devices":

                    response = message_pb2.Response()
                    for device in devices:
                        res = response.devices.add()
                        res.id = device['id']
                        res.name = device['name']
                        res.on = device['on']
                        res.atributo.name = device['atributo']['name']
                        res.atributo.value = device['atributo']['value']

                        for action in device['actions']:
                            a = res.actions.add()
                            a.id = action['id']
                            a.name = action['name']
                    client.send(response.SerializeToString())

            if message.type == "POST":
                if message.request.name == "action":
                    device = search_device(message.request.idDevice)
                    if device:
                        device['socket'].send(message.SerializeToString())

            
        except Exception as e:
            print(e)



def thread_send(sock: socket.socket, data):
    try:
        sock.send(data)
    except Exception as e:
        print(e)



def search_device(id: int):
    global devices
    for i in range(len(devices)):
        if devices[i]['id'] == id:
            return devices[i]
    
    return None



def update_device(message, connection, index):
    global devices
    if index == CREATE_DEVICE:
        new_device = {
            'id': message.device.id,
            'name': message.device.name,
            'on': message.device.on,
            'atributo': {
                'name': message.device.atributo.name,
                'value': message.device.atributo.value
            },
            'actions': [],
            'socket': connection
        }
        for action in message.device.actions[:]:
            new_device["actions"].append({
                'id':action.id,
                'name':action.name
            })
        devices.append(new_device)
    else:
        devices[index] = {
            'id': message.device.id,
            'name': message.device.name,
            'on': message.device.on,
            'atributo': {
                'name': message.device.atributo.name,
                'value': message.device.atributo.value
            },
            'actions': [],
            'socket': connection
        }
        for action in message.device.actions:
            devices[index]["actions"].append({
                'id':action.id,
                'name':action.name
            })



main()