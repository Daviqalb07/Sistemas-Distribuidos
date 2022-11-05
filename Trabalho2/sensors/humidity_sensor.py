import pika
import pickle
from numpy.random import normal

class HumiditySensor:
    def __init__(self, mean_humidity, sd_humidity):
        self.mean_humidity = mean_humidity
        self.sd_humidity = sd_humidity

    def connect_to_rabbitmq(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host= 'localhost')
        )

        self.channel = self.connection.channel()
        self.channel.queue_declare(queue= 'humidity')

    def sense(self):
            self.humidity = round(normal(self.mean_humidity, self.sd_humidity))
            send = {
                'tipo': 'sensor',
                'id': 2,
                'nome':'Umidade',
                'valor': self.humidity,
                'unidade': '%'
            }
            self.channel.basic_publish(exchange='', routing_key= 'temperature', body=pickle.dumps(send))
            print(f'enviado: {send}')

    def terminate_sense(self):
        self.connection.close()

    def set_mean_humidity(self, mean_humidity):
        self.mean_humidity = mean_humidity
    
    def get_mean_humidity(self):
        return self.mean_humidity
    
    def get_sd_humidity(self):
        return self.sd_humidity
