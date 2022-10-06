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
    idDevice = int(input("Qual id do dispositivo que deseja realizar a ação: "))
    request.request.idDevice = idDevice
    action = int(input("Qual id da ação que deseja realizar: "))
    request.request.idAction = action
    control_sock.send(request.SerializeToString())

    # data = control_sock.recv(BUFFER_SIZE)
    # response = message_pb2.Response()
    # response.ParseFromString(data)

main()