import pika
import time
import pickle
from numpy.random import normal

class LuminositySensor:
    def __init__(self, mean_luminosity, sd_luminosity):
        self.mean_luminosity = mean_luminosity
        self.sd_luminosity = sd_luminosity
        self.on = True
        self.connect_to_rabbitmq()
    
    
    def connect_to_rabbitmq(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host= 'localhost')
        )

        self.channel = self.connection.channel()
        self.channel.queue_declare(queue= 'luminosity')

    
    def sense(self):
        if self.on:
            self.luminosity = round(normal(self.mean_luminosity, self.sd_luminosity))

            if self.luminosity > 100:
                self.luminosity = 100
            elif self.luminosity < 0:
                self.luminosity = 0
                
            send = self.generate_message()
            try:
                assert self.on
                self.channel.basic_publish(exchange='', routing_key= 'luminosity', body= pickle.dumps(send))
            except:
                pass
            print(f'enviado: {send}')

    
    def terminate_sense(self):
        self.connection.close()
    
    def generate_message(self):
        return {
            'tipo': 'sensor',
            'id': 3,
            'nome':'Luminosidade',
            'status': self.on,
            'valor': self.luminosity,
            'unidade': '%'
        }

    def on_off_sensor(self):
        self.on = not self.on
        send = self.generate_message()
        self.channel.basic_publish(exchange='', routing_key= 'luminosity', body= pickle.dumps(send))

    def set_mean_luminosity(self, mean_luminosity):
        self.mean_luminosity = mean_luminosity
    
    def get_mean_luminosity(self):
        return self.mean_luminosity
    
    def get_sd_luminosity(self):
        return self.sd_luminosity