import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = "136.243.207.157"
port = 17832

# connection to hostname on the port.
s.connect((host, port))

msg = "Hello From Client"
s.send(msg.encode('utf-8'))
# Receive no more than 1024 bytes
tm = s.recv(1024)
print(tm.decode('utf-8'))
s.close()

