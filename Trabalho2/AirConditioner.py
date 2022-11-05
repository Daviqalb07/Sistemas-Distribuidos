import grpc
from concurrent import futures
from threading import Thread
import time

import Protobuf.air_conditioner_pb2 as air_conditioner_pb2
import Protobuf.air_conditioner_pb2_grpc as air_conditioner_pb2_grpc

from sensors.temperature_sensor import TemperatureSensor
from properties import *

class AirConditioner:
    def __init__(self, temperature: int, sensor: TemperatureSensor) -> None:
        self.on = True
        self.temperature = temperature
        self.sensor = sensor
        self.sensor.set_mean_temp(self.temperature)


    def OnOffAirCond(self, request, context):
        self.on = not self.on

        response = air_conditioner_pb2.ResponseStatusAirConditioner(status = int(self.on))
        return response

    
    def UpperTemp(self, request, context):
        if self.on:
            self.temperature += 1

            self.sensor.set_mean_temp(self.temperature)

        response = air_conditioner_pb2.ResponseTemperatureAirConditioner(temperature= self.temperature)
        return response


    def LowerTemp(self, request, context):
        if self.on:
            self.temperature -= 1

            self.sensor.set_mean_temp(self.temperature)

        response = air_conditioner_pb2.ResponseTemperatureAirConditioner(temperature = self.temperature)
        return response


def sense(sensor: TemperatureSensor):
    sensor.connect_to_rabbitmq()
    while True:
        try:
            sensor.sense()
            print(f"Média: {sensor.get_mean_temp()}")
            time.sleep(5)
        except:
            break
    sensor.terminate_sense()

temperature_sensor = TemperatureSensor(24, 1)
air_conditioner = AirConditioner(24, temperature_sensor)

Thread(target= sense, args= [temperature_sensor]).start()

server = grpc.server(futures.ThreadPoolExecutor(max_workers= 10))
air_conditioner_pb2_grpc.add_AirConditionerServicer_to_server(air_conditioner, server)

server.add_insecure_port(f"localhost:{AIR_CONDITIONER_PORT}")
server.start()
server.wait_for_termination()