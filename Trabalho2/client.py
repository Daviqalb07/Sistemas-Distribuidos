import socket
import sys
import os
from threading import Thread
import pickle
import time

from properties import *

sensors = []
devices = []

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
    
    Thread(target= thread_dashboard, args= [client]).start()
    Thread(target= thread_recv, args= [client]).start()


def thread_dashboard(client: socket.socket):
    global sensors, devices

    while True:
        clear_terminal()
        print("==================== SmartOffice ====================")
        for device in devices:
            print(f"[x] Device: {device['name']}")
            print(f"\tStatus: {device['status']}")
            if device['measure']:
                print(f"\t{device['measure']}: {device['value']} {device['unity']}\n")
        
        print()
        for sensor in sensors:
            print(f"[+] Sensor: {sensor['nome']}")
            print(f"\tStatus: {sensor['status']}")
            print(f"\tValor: {sensor['valor']} {sensor['unidade']}")

        print()
        print(" 0 - Atualizar dashboard")
        print(" 1 - Ligar/Desligar Lâmpada")
        print(" 2 - Ligar/Desligar Ar Condicionado")
        print(" 3 - Aumentar temperatura do Ar Condicionado")
        print(" 4 - Diminuir temperatura do Ar Condicionado")
        print(" 5 - Ligar/Desligar Umidificador")
        print(" 6 - Aumentar umidificação")
        print(" 7 - Diminuir umidificação")

        print(" 8 - Ligar/Desligar Sensor de Luminosidade")
        print(" 9 - Ligar/Desligar Sensor de Temperatura")
        print("10 - Ligar/Desligar Sensor de Umidade")
        option_select = input("Selecione qual método deseja utilizar: ")

        client.send(option_select.encode('utf-8'))


def thread_recv(client: socket.socket):
    global sensors, devices
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
                        'status': 'Ligado' if json['status'] else 'Desligado',
                        'valor': json['valor'],
                        'unidade': json['unidade']
                    })

                else:
                    sensors[index_sensor]['status'] = 'Ligado' if json['status'] else 'Desligado'
                    sensors[index_sensor]['valor'] = json['valor']
            
            elif json['tipo'] == "device":
                index_device = search_device(json['name'])
                if index_device < 0:
                    devices.append({
                        'name': json['name'],
                        'status': 'Ligado' if json['status'] else 'Desligado',
                        'measure': json['measure'],
                        'value': json['value'],
                        'unity': json['unity']
                    })
                else:
                    devices[index_device]['status'] = 'Ligado' if json['status'] else 'Desligado'
                    devices[index_device]['value'] = json['value']

        except:
            pass


def search_sensor(id_sensor):
    global sensors

    for index, sensor in enumerate(sensors):
        if sensor['id'] == id_sensor:
            return index
    
    return -1

def search_device(name_device):
    global devices

    for index, device in enumerate(devices):
        if device['name'] == name_device:
            return index
    return -1

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

main()