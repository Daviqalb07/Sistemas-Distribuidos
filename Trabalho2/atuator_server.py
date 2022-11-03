from concurrent import futures

import grpc
import Protobuf.message_pb2 as message_pb2
import Protobuf.message_pb2_grpc as message_pb2_grpc

class Control(message_pb2_grpc.GreeterServicer):
    def OnLamp(self, request, context):
        print("Requisição recebida: ")
        print(request)
        response = message_pb2.Response()
        response.Status = True      
        return response

    def OffLamp(self, request, context):
        print("Requisição recebida: ")
        print(request)
        response = message_pb2.Response()
        response.Status = False      
        return response
    
    def OnAirCond(self, request, context):
        print("Requisição recebida: ")
        print(request)
        response = message_pb2.Response()
        response.Status = True      
        return response

    def OffAirCond(self, request, context):
        print("Requisição recebida: ")
        print(request)
        response = message_pb2.Response()
        response.Status = False      
        return response
    
    def OnHumid(self, request, context):
        print("Requisição recebida: ")
        print(request)
        response = message_pb2.Response()
        response.Status = True      
        return response

    def OffHumid(self, request, context):
        print("Requisição recebida: ")
        print(request)
        response = message_pb2.Response()
        response.Status = False      
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_pb2_grpc.add_GreeterServicer_to_server(Control(), server)
    server.add_insecure_port("localhost:8282")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()