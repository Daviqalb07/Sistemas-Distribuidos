import pika
import time
import pickle
from numpy.random import uniform

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host= 'localhost')
)

channel = connection.channel()
channel.queue_declare(queue= 'temperature')


while True:
    try:
        send = {
            'tipo': 'sensor',
            'id': 1,
            'nome':'temperatura',
            'valor': round(uniform(15, 35), 2)
        }
        channel.basic_publish(exchange='', routing_key= 'temperature', body=pickle.dumps(send))
        print(f'enviado: {send}')
        time.sleep(5)
        
    except:
        break
connection.close()