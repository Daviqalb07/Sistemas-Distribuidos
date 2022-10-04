import socket
import sys
import threading
import device_pb2
import messages_pb2

GATEWAY_ADDRESS = "localhost"
GATEWAY_PORT = 8181
BUFFER_SIZE = 1024

def main():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        print("Não deu certo :(")
        sys.exit(1)

    try:
        server.bind((GATEWAY_ADDRESS, GATEWAY_PORT))
        print(f"Server on na porta {GATEWAY_PORT} ! :D")
    except:
        print(f"Porta {GATEWAY_PORT} ocupada, tente novamente!")
        sys.exit(1)

    server.listen()

    while True:
        try:
            client, _ = server.accept()
            threading.Thread(target= thread_client, args= [client]).start()
        except:
            break
        

def thread_client(client: socket.socket):
    while True:
        try:
            message = messages_pb2.Request()
            data = client.recv(BUFFER_SIZE)
            print(data)
            message.ParseFromString(data)

            print(message.type)
            
        except Exception as e:
            print(e)
            break

main()