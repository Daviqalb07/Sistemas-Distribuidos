import socket
import threading
import sys
import pickle
from properties import *

def main():
    nickname = input("Digite seu username: ")
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        print("Não deu certo :(")
        sys.exit(1)

    try:
        client.connect((SERVER_ADDRESS, SERVER_PORT))
        client.send(bytes(nickname, 'utf-8'))
    except socket.gaierror as e:
        print("Address-related error: %s" % e)
        sys.exit(1)
    except socket.error as e:
        print("Error connecting to server: %s" % e)
        sys.exit(1)


    threading.Thread(target= send, args= [client, nickname]).start()
    threading.Thread(target= receive, args= [client]).start()

    while True:
        pass

    client.close()

def send(client: socket.socket, nickname: str):
    while True:
        message = input()
        object = message_json(nickname, message)
        try:
            client.send(pickle.dumps(object))
        except:
            print("Erro ao enviar")

def receive(client: socket.socket):
    while True:
        try:
            receive = client.recv(4096)
            object = pickle.loads(receive)

            if object['message'] != "":
                print(f"{object['nickname']}: {object['message']}")
        except:
            print("Erro ao receber")

def message_json(nickname:str, message: str):
    return {
        'nickname': nickname,
        'message': message
    }

main()