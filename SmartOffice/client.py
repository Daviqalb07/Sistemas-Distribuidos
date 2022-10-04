import socket
import sys
import message_pb2
from properties import *

def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as e:
        print(e)
        sys.exit(1)

    try:
        client.connect((GATEWAY_ADDRESS, GATEWAY_PORT))
    except:
        print(e)
        sys.exit(1)
    
    message_join_client = message_pb2.Message(type= "CLIENT_JOIN")