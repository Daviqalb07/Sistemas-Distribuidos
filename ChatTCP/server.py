import socket
import sys
import threading
from properties import *


class Client:
    def __init__(self, nickname: str, sock: socket.socket):
        self.nickname = nickname
        self.sock = sock
    
    def get_nickname(self):
        return self.nickname
    
    def get_sock(self):
        return self.sock

clientList = []

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
            client = Client(client_nickname, client_sock)
            threading.Thread(target= thread_client, args= [client]).start()
            clientList.append(client)
        except:
            break


    


def thread_client(client: Client):
    while True:
        try:
            msg = client.get_sock().recv(4096)
        except socket.error as error:
            print(error)
            break
        if not msg:
            break
        for cli in clientList:
            if cli != client:
                try:
                    cli.get_sock().send(msg)
                except socket.error as error:
                    print(error)
    
    client.close()
    
    

main()