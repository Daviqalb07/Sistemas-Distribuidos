import socket
from threading import Thread
from properties import *

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def receive():
    global client_socket
    response = client_socket.recv(BUFFER_SIZE).decode("utf-8")
    print(f"O resultado é: {response}")

while True:
    request = input("Escreva a operacao que deseja realizar:\n")
    client_socket.sendto(bytes(request, 'utf-8'), (HOST, PORT))
    Thread(target= receive).start()