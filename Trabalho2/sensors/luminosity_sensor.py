import pika
import time
import pickle
from numpy.random import normal

class LuminositySensor:
    def __init__(self, mean_luminosity, sd_luminosity):
        self.mean_luminosity = mean_luminosity
        self.sd_luminosity = sd_luminosity

        self.connect_to_rabbitmq()
    
    
    def connect_to_rabbitmq(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host= 'localhost')
        )

        self.channel = self.connection.channel()
        self.channel.queue_declare(queue= 'luminosity')

    
    def sense(self):
            self.luminosity = round(normal(self.mean_luminosity, self.sd_luminosity))
            send = {
                'tipo': 'sensor',
                'id': 3,
                'nome':'Luminosidade',
                'valor': self.luminosity,
                'unidade': '%'
            }
            self.channel.basic_publish(exchange='', routing_key= 'luminosity', body=pickle.dumps(send))
            print(f'enviado: {send}')

    
    def terminate_sense(self):
        self.connection.close()
    
    
    def set_mean_luminosity(self, mean_luminosity):
        self.mean_luminosity = mean_luminosity
    
    def get_mean_luminosity(self):
        return self.mean_luminosity
    
    def get_sd_luminosity(self):
        return self.sd_luminosity