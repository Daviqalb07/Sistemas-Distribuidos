import pika
import pickle
from numpy.random import normal

class HumiditySensor:
    def __init__(self, mean_humidity, sd_humidity):
        self.mean_humidity = mean_humidity
        self.sd_humidity = sd_humidity
        self.on = True

    def connect_to_rabbitmq(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host= 'localhost')
        )

        self.channel = self.connection.channel()
        self.channel.queue_declare(queue= 'humidity')

    def sense(self):
        if self.on:
            self.humidity = round(normal(self.mean_humidity, self.sd_humidity))
            
            if self.humidity > 100:
                self.humidity = 100
            if self.humidity < 0:
                self.humidity = 0
                
            send = self.generate_message()
            try:
                assert self.on
                self.channel.basic_publish(exchange='', routing_key= 'humidity', body=pickle.dumps(send))
            except:
                pass
            print(f'enviado: {send}')

    def terminate_sense(self):
        self.connection.close()

    def generate_message(self):
        return {
            'tipo': 'sensor',
            'id': 2,
            'nome':'Umidade',
            'status': self.on,
            'valor': self.humidity,
            'unidade': '%'
        }

    def on_off_sensor(self):
        self.on = not self.on
        send = self.generate_message()
        self.channel.basic_publish(exchange='', routing_key= 'humidity', body=pickle.dumps(send))

    def set_mean_humidity(self, mean_humidity):
        self.mean_humidity = mean_humidity
    
    def get_mean_humidity(self):
        return self.mean_humidity
    
    def get_sd_humidity(self):
        return self.sd_humidity
