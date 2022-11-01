import socket
import pika
import pickle
import sys
from threading import Thread

import grpc
import GRPC.Protobuf.message_pb2 as message_pb2
import GRPC.Protobuf.message_pb2_grpc as message_pb2_grpc

HOME_ASSISTANT_ADDRESS = 'localhost'
HOME_ASSISTANT_PORT = 8181
BUFF_SIZE = 1024


def main():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOME_ASSISTANT_ADDRESS, HOME_ASSISTANT_PORT))
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
    with grpc.insecure_channel('localhost:8282') as channel:
        stub = message_pb2_grpc.GreeterStub(channel)
        while True:
            try:
                msg = client.recv(BUFF_SIZE).decode('utf-8')

                if(msg == '1'):
                    # Enviar valor do Sensor
                    request = message_pb2.Request(Value = 60) 
                    response = stub.OnLamp(request)
                    print(f"O Status da Lâmpada: {response.Status}")

                elif(msg == '2'):
                    # Enviar valor do Sensor
                    request = message_pb2.Request(Value = 10)
                    response = stub.OffLamp(request)
                    print(f"O Status da Lâmpada: {response.Status}")

                elif(msg == '3'):
                    # Enviar valor do Sensor
                    request = message_pb2.Request(Value = 30) 
                    response = stub.OnAirCond(request)
                    print(f"O Status do Ar Condicionado: {response.Status}")

                elif(msg == '4'):
                    # Enviar valor do Sensor
                    request = message_pb2.Request(Value = 20)
                    response = stub.OffAirCond(request)
                    print(f"O Status do Ar Condicionado: {response.Status}")

                elif(msg == '5'):
                    # Enviar valor do Sensor
                    request = message_pb2.Request(Value = 70) 
                    response = stub.OnHumid(request)
                    print(f"O Status do Umidificador: {response.Status}")

                elif(msg == '6'):
                    # Enviar valor do Sensor
                    request = message_pb2.Request(Value = 20)
                    response = stub.OffHumid(request)
                    print(f"O Status do Umidificador: {response.Status}")

                else:
                    print("Método Inexistente")
                    break

            except Exception as e:
                print(e)
                break

