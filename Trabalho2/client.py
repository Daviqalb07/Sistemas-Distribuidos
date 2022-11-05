import socket
import sys
import os
from threading import Thread

from properties import *

def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as e:
        print(e)
        sys.exit(1)
    
    try:
        client.connect((HOME_ASSISTANT_HOST, HOME_ASSISTANT_PORT))
    except Exception as e:
        print(e)
        sys.exit(1)
    

    Thread(target= thread_print).start()
    Thread(target= thread_input).start()

def thread_print():
    while True:
        print("1 - Ligar/Desligar Lâmpada")
        print("2 - Ligar/Desligar o Ar Condicionado")
        print("3 - Aumentar temperatura do Ar Condicionado")
        print("4 - Diminuir temperatura do Ar Condicionado")
        print("5 - Ligar/Desligar o Umidificador")
        print("6 - Velocidade alta do Umidificador")
        print("7 - Velocidade baixa do Umidificador\n")

        print("Selecione qual método deseja utilizar: ")
        clear_terminal()

def thread_input(client: socket.socket):
    while True:    
        option_select = input()
        client.send(option_select.encode('utf-8'))


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

main()