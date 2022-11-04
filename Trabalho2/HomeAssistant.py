import socket
import pika
import pickle
import sys
from threading import Thread

import grpc
import Protobuf.message_pb2 as message_pb2
import Protobuf.message_pb2_grpc as message_pb2_grpc

import Protobuf.air_conditioner_pb2 as air_conditioner_pb2
import Protobuf.air_conditioner_pb2_grpc as air_conditioner_pb2_grpc

import Protobuf.humidifier_pb2 as humidifier_pb2
import Protobuf.humidifier_pb2_grpc as humidifier_pb2_grpc

import Protobuf.lamp_pb2 as lamp_pb2
import Protobuf.lamp_pb2_grpc as lamp_pb2_grpc

from properties import *

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
        Thread(target= thread_recv_client, args= [client]).start()


def callback(ch, method, properties, body):
    print(f"[x] mensagem recebida: {pickle.loads(body)}")

def thread_queue(queue: str):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host= 'localhost')
    )
    channel = connection.channel()

    channel.queue_declare(queue= queue)
    channel.basic_consume(queue= queue, on_message_callback= callback, auto_ack= True)
    channel.start_consuming()

def thread_recv_client(client: socket.socket):
    with grpc.insecure_channel('localhost:8184') as channel:
        stub = lamp_pb2_grpc.LampStub(channel)
        while True:
            try:
                msg = client.recv(BUFF_SIZE).decode('utf-8')

                if(msg == '1'):
                    # Enviar valor do Sensor
                    request = lamp_pb2.RequestLamp(Value = 60) 
                    response = stub.OnOffLamp(request)
                    print(f"O Status da Lâmpada: {response.status}")

                elif(msg == '2'):
                    # Enviar valor do Sensor
                    request = message_pb2.Request(Value = 10)
                    response = stub.OffLamp(request)
                    print(f"O Status da Lâmpada: {response.Status}")

                elif(msg == '3'):
                    # Enviar valor do Sensor
                    request = air_conditioner_pb2.RequestAirConditioner(Value = 30) 
                    response = stub.OnOffAirCond(request)
                    print(f"O Status do Ar Condicionado: {response.status}")

                elif(msg == '4'):
                    # Enviar valor do Sensor
                    request = air_conditioner_pb2.RequestAirConditioner(Value = 20)
                    response = stub.UpperTemp(request)
                    print(f"Temperatura: {response.temperature}")

                elif(msg == '5'):
                    # Enviar valor do Sensor
                    request = humidifier_pb2.RequestHumidifier(Value = 70) 
                    response = stub.OnOffHumidifier(request)
                    print(f"O Status do Umidificador: {response.status}")

                elif(msg == '6'):
                    # Enviar valor do Sensor
                    request = humidifier_pb2.RequestHumidifier(Value = 20)
                    response = stub.HighVelocity(request)
                    print(f"Velocidade do Umidificador: {response.velocity}%")
                
                elif(msg == '7'):
                    # Enviar valor do Sensor
                    request = humidifier_pb2.RequestHumidifier(Value = 20)
                    response = stub.LowVelocity(request)
                    print(f"Velocidade do Umidificador: {response.velocity}%")

                else:
                    print("Método Inexistente")
                    break

            except Exception as e:
                print(e)
                break

main ()