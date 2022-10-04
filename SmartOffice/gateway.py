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
        server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    except:
        print("Não deu certo :(")
        sys.exit(1)

    try:
        server_tcp.bind((GATEWAY_ADDRESS, GATEWAY_PORT))
        print(f"Server on na porta {GATEWAY_PORT} ! :D")
    except:
        print(f"Porta {GATEWAY_PORT} ocupada, tente novamente!")
        sys.exit(1)

    threading.Thread(target= discovery_devices, args= [server_udp]).start()
    server_tcp.listen()
    while True:
        try:
            client, _ = server_tcp.accept()
            threading.Thread(target= thread_client, args= [client]).start()
        except:
            break
        
def discovery_devices(server_udp: socket.socket):
    server_udp.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    while True:
        server_udp.sendto(bytes(f"{GATEWAY_ADDRESS} {GATEWAY_PORT}", encoding='utf-8'), ("224.1.1.1", 5001))

def thread_client(client: socket.socket):
    while True:
        try:
            message = messages_pb2.Request()
            data = client.recv(BUFFER_SIZE)
            message.ParseFromString(data)

            print(message.sensor.value)
            
        except Exception as e:
            print(e)
            break

main()