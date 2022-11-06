import pika
import pickle
from numpy.random import normal


class TemperatureSensor:
    def __init__(self, mean_temp, sd_temp):
        self.mean_temp = mean_temp
        self.sd_temp = sd_temp
        self.on = True
        self.connect_to_rabbitmq()
    
    
    def connect_to_rabbitmq(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host= 'localhost')
        )

        self.channel = self.connection.channel()
        self.channel.queue_declare(queue= 'temperature')

    
    def sense(self):
        if self.on:
            self.temperature = round(normal(self.mean_temp, self.sd_temp))
            
            send = self.generate_message()
            try:
                assert self.on
                self.channel.basic_publish(exchange='', routing_key= 'temperature', body=pickle.dumps(send))
            except:
                pass
            print(f'enviado: {send}')

    
    def terminate_sense(self):
        self.connection.close()
    
    def generate_message(self):
        return {
            'tipo': 'sensor',
            'id': 1,
            'nome':'Temperatura',
            'status': self.on,
            'valor': self.temperature,
            'unidade': '°C'
        }

    def on_off_sensor(self):
        self.on = not self.on
        send = self.generate_message()
        self.channel.basic_publish(exchange='', routing_key= 'temperature', body=pickle.dumps(send))

        
    def set_mean_temp(self, mean_temp):
        self.mean_temp = mean_temp
    
    def get_mean_temp(self):
        return self.mean_temp
    
    def get_sd_temp(self):
        return self.sd_temp

    def get_status(self):
        return self.on
    