import socket
import sys
import time
import message_pb2
from properties import *

def main():
    try:
        control_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as e:
        print(e)
        sys.exit(1)

    try:
        message_join = message_pb2.Message()
        message_join.type = "CLIENT_JOIN"
        control_sock.connect((GATEWAY_ADDRESS, GATEWAY_PORT))
        time.sleep(1)
        control_sock.send(message_join.SerializeToString())
    except:
        print(e)
        sys.exit(1)
    

    request = message_pb2.Message()
    request.type = "POST"
    request.request.name = "action"
    request.request.idDevice = 2
    control_sock.send(request.SerializeToString())

    data = control_sock.recv(BUFFER_SIZE)
    response = message_pb2.Response()
    response.ParseFromString(data)


    action = int(input("Qual ação deseja realizar: "))
    # for device in response.devices:
    #     print(f"Device: {device.name}")
    #     print(f"\tid: {device.id}")
    #     print("\tSensor:")
    #     print(f"\t\tNome: {device.sensor.name}")
    #     print(f"\t\tValor: {device.sensor.value}")
    #     print("\tAções possíveis:")
    #     for action in device.actions:
    #         print(f"\t\t{action.id} - {action.name}")
    #     print()


main()