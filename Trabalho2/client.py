import socket
import sys

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
    
    while True:
        print("1 - Ligar a Lâmpada")
        print("2 - Desligar a Lâmpada")
        print("3 - Ligar o Ar Condicionado")
        print("4 - Desligar o Ar Condicionado")
        print("5 - Ligar o Umidificador")
        print("6 - Desligar o Umidificador")
        option_select = input("Selecione qual método deseja utilizar: ")

        client.send(option_select.encode('utf-8'))
        print()



main()