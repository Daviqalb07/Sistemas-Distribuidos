import pika
import time
import pickle
from numpy.random import uniform

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host= 'localhost')
)

channel = connection.channel()
channel.queue_declare(queue= 'humidity')


while True:
    try:
        send = {
            'tipo': 'sensor',
            'id': 2,
            'nome':'umidade',
            'valor': round(uniform(0, 100), 2)
        }
        channel.basic_publish(exchange='', routing_key= 'humidity', body=pickle.dumps(send))
        print(f'enviado: {send}')
        time.sleep(5)
    except:
        break
connection.close()