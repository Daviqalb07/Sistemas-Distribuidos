import grpc
from concurrent import futures

import Protobuf.lamp_pb2 as lamp_pb2
import Protobuf.lamp_pb2_grpc as lamp_pb2_grpc

from properties import *

class Lamp:
    def __init__(self):
        self.on = True
    

    def OnOffLamp(self, request, context):
        self.on = not self.on
        response = lamp_pb2.ResponseLamp(status = self.on)
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers= 10))
lamp_pb2_grpc.add_LampServicer_to_server(Lamp(), server)
server.add_insecure_port(f"localhost:{LAMP_PORT}")
server.start()
server.wait_for_termination()