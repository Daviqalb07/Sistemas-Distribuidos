import socket
import pika
import pickle
import sys
from threading import Thread

import grpc
import Protobuf.air_conditioner_pb2 as air_conditioner_pb2
import Protobuf.air_conditioner_pb2_grpc as air_conditioner_pb2_grpc

import Protobuf.humidifier_pb2 as humidifier_pb2
import Protobuf.humidifier_pb2_grpc as humidifier_pb2_grpc

import Protobuf.lamp_pb2 as lamp_pb2
import Protobuf.lamp_pb2_grpc as lamp_pb2_grpc

from properties import *

clients = []
devices = {
    'Ar-condicionado': None,
    'Lampada': None,
    'Umidificador': None
}

def main():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOME_ASSISTANT_HOST, HOME_ASSISTANT_PORT))
    except Exception as e:
        print(e)
        sys.exit(1)

    temperature_thread = Thread(target= thread_queue, args= ['temperature'])
    temperature_thread.start()

    humidity_thread = Thread(target= thread_queue, args= ['humidity'])
    humidity_thread.start()

    luminosity_thread = Thread(target= thread_queue, args= ['luminosity'])
    luminosity_thread.start()

    server.listen()
    while True:
        client, _ = server.accept()
        clients.append(client)
        Thread(target= thread_recv_client, args= [client]).start()
        Thread(target= thread_send_devices, args= [client]).start()


    

def callback(ch, method, properties, body):
    global clients

    for client in clients:
        client.send(body)


def thread_queue(queue: str):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host= 'localhost')
    )
    channel = connection.channel()

    channel.queue_declare(queue= queue)
    channel.basic_consume(queue= queue, on_message_callback= callback, auto_ack= True)
    channel.start_consuming()


def thread_send_devices(client: socket.socket):
    global devices

    while True:
        for key in devices.keys():
            if devices[key]:
                client.send(pickle.dumps(devices[key]))


def thread_recv_client(client: socket.socket):
    stub_lamp = lamp_pb2_grpc.LampStub(grpc.insecure_channel(f'localhost:{LAMP_PORT}'))
    stub_air_conditioner = air_conditioner_pb2_grpc.AirConditionerStub(grpc.insecure_channel(f'localhost:{AIR_CONDITIONER_PORT}'))
    stub_humidifier = humidifier_pb2_grpc.HumidifierStub(grpc.insecure_channel(f'localhost:{HUMIDIFIER_PORT}'))
    
    update_air_conditioner(stub_air_conditioner.GetAirCondInfo(air_conditioner_pb2.RequestAirConditioner()))
    # COLOCAR PARA OS OUTROS DEVICES
    while True:
        try:
            msg = client.recv(BUFF_SIZE).decode('utf-8')

            if(msg == '1'):
                request = lamp_pb2.RequestLamp() 
                response = stub_lamp.OnOffLamp(request)
                print(f"O Status da Lâmpada: {response.status}")
                update_lamp(response)

            elif(msg == '2'):
                request = air_conditioner_pb2.RequestAirConditioner() 
                response = stub_air_conditioner.OnOffAirCond(request)
                print(f"O Status do Ar Condicionado: {response.status}")
                update_air_conditioner(response)

            elif(msg == '3'):
                request = air_conditioner_pb2.RequestAirConditioner()
                response = stub_air_conditioner.UpperTemp(request)
                print(f"Temperatura: {response.temperature}")
                update_air_conditioner(response)
            
            elif(msg == '4'):
                request = air_conditioner_pb2.RequestAirConditioner()
                response = stub_air_conditioner.LowerTemp(request)
                print(f"Temperatura: {response.temperature}")
                update_air_conditioner(response)

            elif(msg == '5'):
                request = humidifier_pb2.RequestHumidifier() 
                response = stub_humidifier.OnOffHumidifier(request)
                print(f"O Status do Umidificador: {response.status}")
                update_humidifier(response)

            elif(msg == '6'):
                request = humidifier_pb2.RequestHumidifier()
                response = stub_humidifier.UpperHumid(request)
                print(f"Umidade configurada: {response.humidity}%")
                update_humidifier(response)
            
            elif(msg == '7'):
                request = humidifier_pb2.RequestHumidifier()
                response = stub_humidifier.LowerHumid(request)
                print(f"Umidade configurada: {response.humidity}%")
                update_humidifier(response)

            else:
                print("Método Inexistente")
                break

        except Exception as e:
            print(e)
            break

def update_air_conditioner(response):
    global devices

    devices['Ar-condicionado'] = {
        'tipo': 'device',
        'name': 'Ar-condicionado',
        'status': response.status,
        'measure': 'Temperatura',
        'value': response.temperature,
        'unity': '°C'
    }

def update_humidifier(response):
    global devices

    devices['Umidificador'] = {
        'tipo': 'device',
        'name': 'Umidificador',
        'status': response.status,
        'measure': 'Umidade',
        'value': response.humidity,
        'unity': '%'
    }

def update_lamp(response):
    global devices

    devices['Lâmpada'] = {
        'tipo': 'device',
        'name': 'Lâmpada',
        'status': response.status,
        'measure': None,
        'value': None,
        'unity': None
    }
main ()