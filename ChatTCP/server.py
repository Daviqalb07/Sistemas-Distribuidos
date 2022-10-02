import pickle
import socket
import sys
import threading
from properties import *

SERVER_ADDRESS = "localhost"
SERVER_PORT = 8181

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
        print(f"Server on na porta {SERVER_PORT} ! :D")
    except:
        print(f"Porta {SERVER_PORT} ocupada, tente novamente!")
        sys.exit(1)

    server.listen()

    while True:
        try:
            client_sock, _ = server.accept()
            client_nickname = client_sock.recv(4096).decode('utf-8')
            threading.Thread(target= thread_client, args= [client_sock, client_nickname]).start()
            clients_sockets.append(client_sock)
            clients_nicknames.append(client_nickname)

        except:
            break
        


def thread_client(client: socket.socket, client_nickname: str):
    global clients_nicknames, clients_sockets
    while True:
        try:
            object_bytes = client.recv(4096)
            object = pickle.loads(object_bytes)

        except socket.error as error:
            print(f"{error} de nickname: {client_nickname}")
            break
        if object['message'].upper() == "/USUARIOS":
            response = response_json(SERVER_RESPONSE_USERS, clients_nicknames)
            client.send(pickle.dumps(response))
        
        elif object['message'].upper() == "/SAIR":
            object['message'] = "saiu"
            object_bytes = pickle.dumps(object)

            for cli in clients_sockets:
                if cli != client:
                    try:
                        cli.send(object_bytes)
                    except socket.error as error:
                        print(error)
            
            response = response_json(CLIENT_QUIT, f"{object['nickname']} {object['message']}")
            try:
                client.send(pickle.dumps(response))
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