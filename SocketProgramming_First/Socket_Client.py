import socket
import sys

try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
    sys.exit()

print('Socket Created')

host = 'dspcard.ir'
port = 25

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

print('Ip address of ' + host + ' is ' + remote_ip)
s.connect((remote_ip, port))
print('Socket Connected to ' + host + ' on ip ' + remote_ip)

message = "GET / HTTP/1.1\r\n\r\n"
try:
    # Set the whole string
    s.sendto(message.encode('utf-8'),(host,port))
except socket.error:
    print('Send failed')
    sys.exit()

print('Message send successfully')
data = s.recv(4096)
print(data.decode('utf-8'))
s.close()