import grpc
import Protobuf.message_pb2 as message_pb2
import Protobuf.message_pb2_grpc as message_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:8282') as channel:
        stub = message_pb2_grpc.GreeterStub(channel)
        while True:
            print("1 - Ligar a Lâmpada")
            print("2 - Desligar a Lâmpada")
            print("3 - Ligar o Ar Condicionado")
            print("4 - Desligar o Ar Condicionado")
            print("5 - Ligar o Umidificador")
            print("6 - Desligar o Umidificador")
            OptionSelect = input("Selecione qual método deseja utilizar: ")
            if(OptionSelect == '1'):
                # Enviar valor do Sensor
                request = message_pb2.Request(Value = 60) 
                response = stub.OnLamp(request)
                print(f"O Status da Lâmpada: {response.Status}")
            elif(OptionSelect == '2'):
                # Enviar valor do Sensor
                request = message_pb2.Request(Value = 10)
                response = stub.OffLamp(request)
                print(f"O Status da Lâmpada: {response.Status}")
            elif(OptionSelect == '3'):
                # Enviar valor do Sensor
                request = message_pb2.Request(Value = 30) 
                response = stub.OnAirCond(request)
                print(f"O Status do Ar Condicionado: {response.Status}")
            elif(OptionSelect == '4'):
                # Enviar valor do Sensor
                request = message_pb2.Request(Value = 20)
                response = stub.OffAirCond(request)
                print(f"O Status do Ar Condicionado: {response.Status}")
            elif(OptionSelect == '5'):
                # Enviar valor do Sensor
                request = message_pb2.Request(Value = 70) 
                response = stub.OnHumid(request)
                print(f"O Status do Umidificador: {response.Status}")
            elif(OptionSelect == '6'):
                # Enviar valor do Sensor
                request = message_pb2.Request(Value = 20)
                response = stub.OffHumid(request)
                print(f"O Status do Umidificador: {response.Status}")
            else:
                print("Método Inexistente")
                break
            print()

if __name__ == "__main__":
    run()