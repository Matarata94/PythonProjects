from threading import *
import socket as sc
import time
import json
from ChatAppProject.Database import *


class ConnectionThread(Thread):
    strRecieved=[]
    def __init__(self, socket, address, recieveBuffer):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.recieveBuffer = recieveBuffer
        self.dbObject = DatabaseHandler()
        self.start()
        self._stop = Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def run(self, timeout=40):
        self.sock.setsockopt(sc.IPPROTO_TCP, sc.TCP_NODELAY, 1)
        self.sock.setblocking(0)
        begin = time.time()
        while 1:
            if time.time() - begin > timeout:
                break

            try:
                self.strRecieved = self.sock.recv(self.recieveBuffer).decode('utf-8')
                if self.strRecieved:
                    tempJson = json.loads(self.strRecieved)
                    if tempJson['requestType'] == 'register':
                        queryUsername = self.dbObject.queryFromDB('users','username',tempJson['username'],'register')
                        if queryUsername == 'empty':
                            insertResult = self.dbObject.insertUserToDB(tempJson['username'], tempJson['password'])
                            print(insertResult + "--> Username: " + tempJson['username'] + " , Password: " + tempJson['password'])
                            pythonDictionary = {'serverJsonResult': insertResult}
                            dictionaryToJson = json.dumps(pythonDictionary)
                            begin = time.time()
                            self.sock.sendall(dictionaryToJson.encode("utf-8"))
                        elif queryUsername != "empty":
                            if queryUsername[2] == tempJson['password']:
                                pythonDictionary = {'serverJsonResult': 'identified'}
                                dictionaryToJson = json.dumps(pythonDictionary)
                                begin = time.time()
                                self.sock.sendall(dictionaryToJson.encode("utf-8"))
                            elif queryUsername[2] != tempJson['password']:
                                pythonDictionary = {'serverJsonResult': 'identify_failed'}
                                dictionaryToJson = json.dumps(pythonDictionary)
                                begin = time.time()
                                self.sock.sendall(dictionaryToJson.encode("utf-8"))
                    elif tempJson['requestType'] == 'msg':
                        insertResult = self.dbObject.insertChatToDB(tempJson['username'], tempJson['msgText'], tempJson['msgDate'])
                        print(tempJson['msgText'],tempJson['msgDate'])
                        pythonDictionary = {'serverJsonResult': insertResult}
                        dictionaryToJson = json.dumps(pythonDictionary)
                        begin = time.time()
                        self.sock.sendall(dictionaryToJson.encode("utf-8"))
                    elif tempJson['requestType'] == 'chatData':
                        queryChats = self.dbObject.queryFromDB('chats','username',tempJson['username'],'chatData')
                        i = 0
                        tempChats = []
                        while len(queryChats) > i:
                            tempChats.insert(i,queryChats[i][2])
                            print(tempChats[i])
                            i+=1
                        #Should send tempCHats to android and process there
                        pythonDictionary = {'serverJsonResult' : 'done'}
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
