import socket
from threading import *
import time

#1000 = p25 (Raspberry Pi)

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = "192.168.1.3"
port = 9999

# bind to the port
serversocket.bind((host, port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()
        self._stop = Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def run(self):
        i=True
        while i:
            tempStr = self.sock.recv(1024).decode()
            if(tempStr != ""):
                print('Client sent:', tempStr)
                msg = "Hello From Server"
                self.sock.send(msg.encode('utf-8'))
                i = False
                self.stop()
                clientsocket.close()
                print("Client Socket Closed!")

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))
    client(clientsocket, addr)

