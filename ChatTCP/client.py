import socket
import threading
import sys
import pickle
from properties import *

quitted = False

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
    global quitted
    while True:
        print()
        message = input()
        if message == "/SAIR":
            quitted = True
        object = message_json(NORMAL_MESSAGE, nickname, message)
        try:
            client.send(pickle.dumps(object))
        except:
            print("Erro ao enviar")

def receive(client: socket.socket):
    global quitted

    while True:
        print()
        try:
            receive = client.recv(4096)
            object = pickle.loads(receive)

            if object['tipo'] == SERVER_RESPONSE_USERS:
                print("Usuários no chat:")
                for username in object['message']:
                    print(username)
            
            elif object['tipo'] == NORMAL_MESSAGE:
                if object['message'] != "":
                    print(f"<{object['nickname']}>: {object['message']}")
                if quitted:
                    client.close()
                    quitted = False
                    sys.exit(0)
    

        except Exception as e:
            print(e)

def message_json(tipo: int, nickname:str, message: str):
    return {
        'tipo': tipo,
        'nickname': nickname,
        'message': message
    }

main()