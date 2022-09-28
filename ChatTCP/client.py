import socket
import threading
import sys
import pickle
from properties import *

quitted_flag = False
quitted = 0
SERVER_ADDRESS = "localhost"
SERVER_PORT = 8181

def main():
    print("Comandos do servidor:")
    print("1 - /ENTRAR <IP> <PORTA>: Para entrar no Chat")
    print("2 - /USUARIOS : Para receber a lista de usuários no chat")
    print("3 - /SAIR : Para sair do chat")

    entrar = ""

    while True:
        entrar = input("Primeiro, entre em algum chat com o /ENTRAR:\n")

        
        entrar_args = entrar.split()
        if len(entrar_args) != 3:
            print("Comando utilizado incorretamente")
            pass
        
        elif entrar_args[0].upper() == "/ENTRAR":
            if entrar_args[1].lower() == "localhost" or entrar_args[1] == "127.0.0.1":
                SERVER_ADDRESS = "localhost"
            else:
                SERVER_ADDRESS = socket.inet_aton(entrar_args[1])
            
            SERVER_PORT = int(entrar_args[2])

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
                if threading.active_count() != 0:
                    pass
                else:
                    break

    client.close()

def send(client: socket.socket, nickname: str):
    global quitted_flag, quitted
    while True:
        print()
        message = input()
        if message == "/SAIR":
            quitted_flag = True
            quitted += 1
            break
        object = message_json(NORMAL_MESSAGE, nickname, message)
        try:
            client.send(pickle.dumps(object))
        except:
            print("Erro ao enviar")
    print("encerrando 1")

def receive(client: socket.socket):
    global quitted_flag, quitted

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
                # if quitted_flag:
                #     client.close()
                #     quitted_flag = False
                #     break
            elif object['tipo'] == CLIENT_QUIT:
                print(object['message'])
                print("entrei no if")
                client.close()
                break
    

        except Exception as e:
            print(e)
    print("encerrando 2")

def message_json(tipo: int, nickname:str, message: str):
    return {
        'tipo': tipo,
        'nickname': nickname,
        'message': message
    }

main()