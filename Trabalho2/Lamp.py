import grpc
from concurrent import futures
from threading import Thread
import time

import Protobuf.lamp_pb2 as lamp_pb2
import Protobuf.lamp_pb2_grpc as lamp_pb2_grpc

from properties import *
from sensors.luminosity_sensor import LuminositySensor

class Lamp:
    def __init__(self, sensor: LuminositySensor) -> None:
        self.on = True
        self.sensor = sensor
        self.sensor.set_mean_luminosity(90)

    def OnOffLamp(self, request, context):
        self.on = not self.on

        if self.on:
            self.sensor.set_mean_luminosity(90)
        else:
            self.sensor.set_mean_luminosity(20)

        response = self.GenerateResponse()
        return response

    def GetLampInfo(self, request, context):
        return self.GenerateResponse()
        
    def GenerateResponse(self):
        response = lamp_pb2.ResponseLamp(
            tipo= "device",
            name= "Lâmpada",
            status= self.on
        )
        return response

def sense(sensor: LuminositySensor):
    sensor.connect_to_rabbitmq()
    while True:
        try:
            sensor.sense()
            print(f"Média: {sensor.get_mean_luminosity()}")
            time.sleep(5)
        except:
            break
    sensor.terminate_sense()

luminosity_sensor = LuminositySensor(50, 10)
lamp = Lamp(luminosity_sensor)

Thread(target= sense, args= [luminosity_sensor]).start()

server = grpc.server(futures.ThreadPoolExecutor(max_workers= 10))
lamp_pb2_grpc.add_LampServicer_to_server(lamp, server)

server.add_insecure_port(f"localhost:{LAMP_PORT}")
server.start()
server.wait_for_termination()