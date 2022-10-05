import socket
import sys
import time
import message_pb2
from properties import *

def main():
    try:
        dashboard_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as e:
        print(e)
        sys.exit(1)

    try:
        message_join = message_pb2.Message()
        message_join.type = "CLIENT_JOIN"
        dashboard_sock.connect((GATEWAY_ADDRESS, GATEWAY_PORT))
        time.sleep(1)
        dashboard_sock.send(message_join.SerializeToString())
    except:
        print(e)
        sys.exit(1)
    

    request = message_pb2.Message()
    request.type = "GET"
    request.request.name = "devices"
    dashboard_sock.send(request.SerializeToString())

    data = dashboard_sock.recv(BUFFER_SIZE)
    response = message_pb2.Response()
    response.ParseFromString(data)

    for device in response.devices:
        print(f"Device: {device.name}")
        print(f"\tid: {device.id}")
        print("\tSensor:")
        print(f"\t\tNome: {device.sensor.name}")
        print(f"\t\tValor: {device.sensor.value}")
        print("\tAções possíveis:")
        for action in device.actions:
            print(f"\t\t{action.id} - {action.name}")
        print()


main()