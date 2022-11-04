import grpc
from concurrent import futures

import Protobuf.humidifier_pb2 as humidifier_pb2
import Protobuf.humidifier_pb2_grpc as humidifier_pb2_grpc

from properties import *

LOW_VELOCITY = 50
HIGH_VELOCITY = 100

class Humidifier:
    def __init__(self, velocity: int) -> None:
        self.on = True
        self.velocity = velocity


    def OnOffHumidifier(self, request, context):
        self.on = not self.on

        response = humidifier_pb2.ResponseStatusHumidifier(status = int(self.on))
        return response


    def HighVelocity(self, request, context):
        self.velocity = HIGH_VELOCITY
        response = humidifier_pb2.ResponseVelocityHumidifier(velocity= self.velocity)
        return response
    

    def LowVelocity(self, request, context):
        self.velocity = LOW_VELOCITY
        response = humidifier_pb2.ResponseVelocityHumidifier(velocity= self.velocity)
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers= 10))
humidifier_pb2_grpc.add_HumidifierServicer_to_server(Humidifier(LOW_VELOCITY), server)
server.add_insecure_port(f"localhost:{HUMIDIFIER_PORT}")
server.start()
server.wait_for_termination()