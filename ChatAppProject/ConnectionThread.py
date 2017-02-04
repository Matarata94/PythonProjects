from threading import *
import socket as sc
import time
import json
from ChatAppProject.Database import *


class ConnectionThread(Thread):
    strRecieved=[]
    def __init__(self, socket, address, recieveBuffer,type):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.recieveBuffer = recieveBuffer
        self.type = type
        self.dbObject = DatabaseHandler()
        self.start()
        self._stop = Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def run(self, timeout=80):
        self.sock.setsockopt(sc.IPPROTO_TCP, sc.TCP_NODELAY, 1)
        self.sock.setblocking(0)
        begin = time.time()
        while 1:
            if time.time() - begin > timeout:
                print('Recieve Timeout...')
                break

            try:
                self.strRecieved = self.sock.recv(self.recieveBuffer).decode('utf-8')
                if self.strRecieved:
                    if self.type == 'register':
                        tempJson = json.loads(self.strRecieved)
                        queryResult = self.dbObject.queryFromDB('users','username',tempJson['username'])
                        if queryResult != tempJson['username']:
                            insertResult = self.dbObject.insertToDB(tempJson['username'], tempJson['password'])
                            print(insertResult)
                            pythonDictionary = {'serverJsonResult': insertResult}
                            dictionaryToJson = json.dumps(pythonDictionary)
                            begin = time.time()
                            self.sock.sendall(dictionaryToJson.encode("utf-8"))
                        elif queryResult == tempJson['username']:
                            pythonDictionary = {'serverJsonResult': 'user_exist'}
                            dictionaryToJson = json.dumps(pythonDictionary)
                            begin = time.time()
                            self.sock.sendall(dictionaryToJson.encode("utf-8"))
                else:
                    # sleep for sometime to indicate a gap
                    time.sleep(0.1)
            except:
                pass

        self.sock.close()
        print('Socket ' + str(self.addr[0]) + ':' + str(self.addr[1]) + ' Closed!')
        self.stop()
