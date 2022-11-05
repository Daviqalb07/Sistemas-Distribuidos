import socket
import sys
import os
from threading import Thread
import pickle

from properties import *

sensors = []
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
    

    #Thread(target= thread_print).start()
    Thread(target= thread_input, args= [client]).start()
    Thread(target= thread_recv, args= [client]).start()

def thread_print():
    while True:
        for sensor in sensors:
            print(f"[x] Sensor: {sensor['nome']}")
            print(f"\t Valor: {sensor['valor']} {sensor['unidade']}")

        print()
        print("1 - Ligar/Desligar Lâmpada")
        print("2 - Ligar/Desligar o Ar Condicionado")
        print("3 - Aumentar temperatura do Ar Condicionado")
        print("4 - Diminuir temperatura do Ar Condicionado")
        print("5 - Ligar/Desligar o Umidificador")
        print("6 - Aumentar umidificação")
        print("7 - Diminuir umidificação\n")
        
        clear_terminal()


def thread_input(client: socket.socket):
    while True:    
        for sensor in sensors:
            print(f"[x] Sensor: {sensor['nome']}")
            print(f"\t Valor: {sensor['valor']} {sensor['unidade']}")

        print()
        print("1 - Ligar/Desligar Lâmpada")
        print("2 - Ligar/Desligar o Ar Condicionado")
        print("3 - Aumentar temperatura do Ar Condicionado")
        print("4 - Diminuir temperatura do Ar Condicionado")
        print("5 - Ligar/Desligar o Umidificador")
        print("6 - Aumentar umidificação")
        print("7 - Diminuir umidificação\n")
        
        option_select = input("Selecione qual método deseja utilizar: ")
        client.send(option_select.encode('utf-8'))
        clear_terminal()


def thread_recv(client:socket.socket):
    global sensors
    while True:
        try:
            msg = client.recv(BUFF_SIZE)
            json = pickle.loads(msg)

            if json['tipo'] == "sensor":
                index_sensor = search_sensor(json['id'])
                if index_sensor < 0:
                    sensors.append({
                        'id': json['id'],
                        'nome': json['nome'],
                        'valor': json['valor'],
                        'unidade': json['unidade']
                    })

                else:
                    sensors[index_sensor]['valor'] = json['valor']

        except:
            pass


def search_sensor(id_sensor):
    global sensors

    for index, sensor in enumerate(sensors):
        if sensor['id'] == id_sensor:
            return index
    
    return -1
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

main()