# UDPPingerServer.py
import random
from socket import *

HOST = '127.0.0.1'
PORT = 12000

def start_server():
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    print('Iniciando...')
    serverSocket.bind((HOST, PORT))
    print('Iniciado!')
    return serverSocket

def main():
    serverSocket = start_server()

    while True:
        rand = random.randint(0, 10)
        message, address = serverSocket.recvfrom(1024)
        print('Pacote recebido, tamanho: ' + str(rand))
        message = message.upper()
        if rand < 4:
            print('Pacote perdido, tamanho: ' + str(rand))
            continue
        serverSocket.sendto(message, address)
        print('Enviando pacote, tamanho: ' + str(len(message)))

if __name__ == "__main__":
    main()