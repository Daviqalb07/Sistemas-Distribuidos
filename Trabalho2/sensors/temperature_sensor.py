import pika
import pickle
from numpy.random import normal


class TemperatureSensor:
    def __init__(self, mean_temp, sd_temp):
        self.mean_temp = mean_temp
        self.sd_temp = sd_temp

        self.connect_to_rabbitmq()
    
    
    def connect_to_rabbitmq(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host= 'localhost')
        )

        self.channel = self.connection.channel()
        self.channel.queue_declare(queue= 'temperature')

    
    def sense(self):
            self.temperature = round(normal(self.mean_temp, self.sd_temp))
            send = {
                'tipo': 'sensor',
                'id': 1,
                'nome':'Temperatura',
                'valor': self.temperature,
                'unidade': '°C'
            }
            self.channel.basic_publish(exchange='', routing_key= 'temperature', body=pickle.dumps(send))
            print(f'enviado: {send}')

    
    def terminate_sense(self):
        self.connection.close()
    
    
    def set_mean_temp(self, mean_temp):
        self.mean_temp = mean_temp
    
    def get_mean_temp(self):
        return self.mean_temp
    
    def get_sd_temp(self):
        return self.sd_temp
    