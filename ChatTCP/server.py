import pickle
import socket
import sys
import threading
from properties import *


# class Client:
#     def __init__(self, nickname: str, sock: socket.socket):
#         self.nickname = nickname
#         self.sock = sock
    
#     def get_nickname(self):
#         return self.nickname
    
#     def get_sock(self) -> socket.socket:
#         return self.sock

clients_sockets = []
clients_nicknames = []

def main():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        print("Não deu certo :(")
        sys.exit(1)

    try:
        server.bind((SERVER_ADDRESS, SERVER_PORT))
        print("Server on! :D")
    except:
        print(f"Porta {SERVER_PORT} ocupada")
        sys.exit(1)

    server.listen()

    while True:
        try:
            client_sock, _ = server.accept()
            client_nickname = client_sock.recv(4096).decode('utf-8')
            threading.Thread(target= thread_client, args= [client_sock]).start()
            clients_sockets.append(client_sock)
            clients_nicknames.append(client_nickname)

        except:
            break


    


def thread_client(client: socket.socket):
    global clients_nicknames, clients_sockets
    while True:
        try:
            object_bytes = client.recv(4096)
            object = pickle.loads(object_bytes)

        except socket.error as error:
            print(error)
            break
        
        if object['message'] == "/USUARIOS":
            response = response_json(SERVER_RESPONSE_USERS, clients_nicknames)
            client.send(pickle.dumps(response))
        
        elif object['message'] == "/SAIR":
            object['message'] = "saiu"
            object_bytes = pickle.dumps(object)

            for cli in clients_sockets:
                try:
                    cli.send(object_bytes)
                except socket.error as error:
                    print(error)
            break

        
        else:
            for cli in clients_sockets:
                if cli != client:
                    try:
                        cli.send(object_bytes)
                    except socket.error as error:
                        print(error)

    clients_sockets.remove(client)
    clients_nicknames.remove(object['nickname'])
    client.close()
    
def response_json(tipo: int, content):
    return {
        'tipo': tipo,
        'message': content
    }

main()