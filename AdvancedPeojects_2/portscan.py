import optparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)

def connScan(tgtHost, tgtPort):
    try:
        connSocket = socket(AF_INET, SOCK_STREAM)
        connSocket.connect((tgtHost,tgtPort))
        msg="hello"
        connSocket.send(msg.encode('utf-8'))
        results = connSocket.recv(100)
        screenLock.acquire()
        print("[+] " + str(tgtPort) + "/tcp open")
    except:
        screenLock.acquire()
        print("[-] " + str(tgtPort) + "/tcp close")
    finally:
        screenLock.release()
        connSocket.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("[+] Cannot resolve " + tgtHost + ": Unknown host")
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print("\n[+] Scan results for: " + tgtName[2])
    except:
        print("\n[+] Scan results for: " + tgtIP)

    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

def Main():
    parser = optparse.OptionParser('usage %proh -H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port[s] seperated by a comma')
    (options, args) = parser.parse_args()
    if(options.tgtHost == None) | (options.tgtPort == None):
        print(parser.usage)
        exit(0)
    else:
        tgtHost = options.tgtHost
        tgtPorts = str(options.tgtPort).split(',')

    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    Main()

