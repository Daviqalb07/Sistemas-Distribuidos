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
        print("1 - Ligar/Desligar Lâmpada")
        print("2 - Ligar/Desligar o Ar Condicionado")
        print("3 - Aumentar temperatura do Ar Condicionado")
        print("4 - Diminuir temperatura do Ar Condicionado")
        print("5 - Ligar/Desligar o Umidificador")
        print("6 - Velocidade alta do Umidificador")
        print("7 - Velocidade baixa do Umidificador")
        option_select = input("Selecione qual método deseja utilizar: ")

        client.send(option_select.encode('utf-8'))
        print()



main()