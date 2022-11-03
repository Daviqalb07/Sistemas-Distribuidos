import grpc
from concurrent import futures

import Protobuf.air_conditioner_pb2 as air_conditioner_pb2
import Protobuf.air_conditioner_pb2_grpc as air_conditioner_pb2_grpc

from properties import *
class AirConditioner:
    def __init__(self, temperature: int) -> None:
        self.on = True
        self.temperature = temperature

    def OnOffAirCond(self, request, context):
        self.on = not self.on

        response = air_conditioner_pb2.ResponseAirConditioner(status = int(self.on))
        return response

    
    def UpperTemp(self, request, context):
        self.temperature += 1

        response = air_conditioner_pb2.ResponseAirConditioner(status = self.temperature)
        return response

    def LowerTemp(self, request, context):
        self.temperature -= 1

        response = air_conditioner_pb2_grpc.ResponseAirConditioner(status = self.temperature)
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers= 10))
air_conditioner_pb2_grpc.add_AirConditionerServicer_to_server(AirConditioner(24), server)
server.add_insecure_port(f"localhost:{AIR_CONDITIONER_PORT}")
server.start()
server.wait_for_termination()