import socket
import sys

# create socket method
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9995
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation Error:",str(msg))

# Bind socket to port and wait 4 client
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port:",str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding Error:",str(msg) + "\n" + "Retrying...")
        socket_bind()

# Establish a connection with client( Socket must be listening)
def socket_accept():
    conn, address = s.accept()
    print("Connection established | IP: " + address[0] + " | PORT: " + str(address[1]))
    send_command(conn)
    conn.close()


def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    socket_create()
    socket_bind()
    socket_accept()

main()