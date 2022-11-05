import grpc
from concurrent import futures
from threading import Thread
import time

import Protobuf.humidifier_pb2 as humidifier_pb2
import Protobuf.humidifier_pb2_grpc as humidifier_pb2_grpc

from properties import *
from sensors.humidity_sensor import HumiditySensor

class Humidifier:
    def __init__(self, humidity: int, sensor: HumiditySensor) -> None:
        self.on = True
        self.humidity = humidity
        self.sensor = sensor
        self.sensor.set_mean_humidity(self.humidity)

    def OnOffHumidifier(self, request, context):
        self.on = not self.on

        response = humidifier_pb2.ResponseStatusHumidifier(status = self.on)
        return response


    def UpperHumid(self, request, context):
        if self.on:
            self.humidity += 10

            self.sensor.set_mean_humidity(self.humidity)
        response = humidifier_pb2.ResponseVelocityHumidifier(humidity= self.humidity)
        return response
    

    def LowerHumid(self, request, context):
        if self.on:
            self.humidity -= 10

            self.sensor.set_mean_humidity(self.humidity)
        response = humidifier_pb2.ResponseVelocityHumidifier(humidity= self.humidity)
        return response

def sense(sensor: HumiditySensor):
    sensor.connect_to_rabbitmq()
    while True:
        try:
            sensor.sense()
            print(f"Média: {sensor.get_mean_humidity()}")
            time.sleep(5)
        except:
            break
    sensor.terminate_sense()

humidity_sensor = HumiditySensor(50, 5)
humidifier = Humidifier(50, humidity_sensor)

Thread(target= sense, args= [humidity_sensor]).start()

server = grpc.server(futures.ThreadPoolExecutor(max_workers= 10))
humidifier_pb2_grpc.add_HumidifierServicer_to_server(humidifier, server)

server.add_insecure_port(f"localhost:{HUMIDIFIER_PORT}")
server.start()
server.wait_for_termination()