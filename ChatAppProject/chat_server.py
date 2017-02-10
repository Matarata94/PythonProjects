from ChatAppProject.ConnectionThread import *
import socket


class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def socketBinding(self):
        self.serversocket.bind((self.host, self.port))
        self.serversocket.listen(5)
        print('Socket binded to: ' + self.host + ':' + str(self.port))

    def socketClose(self):
        self.serversocket.close()

if __name__ == "__main__":
    chatObj = ChatServer('', 4004)
    chatObj.socketBinding()
    while True:
        clientsocket, addr = chatObj.serversocket.accept()

        print("Got a connection from " + str(addr))
        conThreadObj = ConnectionThread(clientsocket,addr, 4096)
