import socket
import sys
from threading import Thread
from properties import *

def calcula(request: str):
    request_split = request.split()
    try:
        n1 = float(request_split[0])
        op = request_split[1]
        n2 = float(request_split[2])
        
        resultado = 0
        if op == '+':
            resultado = n1 + n2
        elif op == '-':
            resultado = n1 - n2
        elif op == '*':
            resultado = n1 * n2
        elif op == '/':
            if n2 == 0:
                return f"{request} = {'Divisao por zero, tente novamente'}"
            else:
                resultado = n1 / n2
    
        return f"{request} = {resultado}"
    except:
        return "Operacao invalida, revise a forma como digitou"

def send(response: str, address):
    global server_socket
    server_socket.sendto(bytes(response, 'utf-8'), address)



server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    server_socket.bind((HOST, PORT))
    print("Status do servidor: ON!")
except:
    print("Erro ao subir servidor...")
    sys.exit(1)

while True:
    data, address = server_socket.recvfrom(BUFFER_SIZE)
    response = calcula(data.decode('utf-8'))

    Thread(target= send, args= [response, address]).start()