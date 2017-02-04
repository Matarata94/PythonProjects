import socket
import time
import json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.3"
port = 30000

s.connect((host, port))
username = input("Message to server: ")
sendData = json.dumps({'Android' : username})
tt = 1
while True:
        if tt == 1:
                s.sendall(sendData.encode('utf-8'))
                tm = s.recv(4096).decode('utf-8')
                print(tm)
                tt=0

#s.close()
#print('Socket Closed!')