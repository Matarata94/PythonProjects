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
                #recieve data from ClientSocket
                self.strRecieved = self.sock.recv(self.recieveBuffer).decode('utf-8')
                if self.strRecieved:
                    tempJson = json.loads(self.strRecieved)
                    #if request from android is for Register
                    if tempJson['requestType'] == 'register':
                        #check if username already exist
                        queryUsername = self.dbObject.queryFromDB('users','username',tempJson['username'],'register')
                        #if username not exist, create a new user and a table for his chats with his opponet and send success message to android
                        if queryUsername == 'empty':
                            insertResult = self.dbObject.insertUserToDB(tempJson['username'], tempJson['password'])
                            #print(insertResult + "--> Username: " + tempJson['username'] + " , Password: " + tempJson['password'])
                            tableCreationResult = self.dbObject.createTable('chats_' + tempJson['username'] + '_' + tempJson['oppponentUsername'])
                            #check if new user created and also his table is created or not
                            if insertResult == 'inserted' & tableCreationResult == 'table created':
                                pythonDictionary = {'serverJsonResult': 'registerDone'}
                                dictionaryToJson = json.dumps(pythonDictionary)
                                begin = time.time()
                                self.sock.sendall(dictionaryToJson.encode("utf-8"))
                            else:
                                pythonDictionary = {'serverJsonResult': 'registerFailed'}
                                dictionaryToJson = json.dumps(pythonDictionary)
                                begin = time.time()
                                self.sock.sendall(dictionaryToJson.encode("utf-8"))
                        #if username exist then check if password is correct or not and send a success or fail message to android
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
                        queryClient1Chats = self.dbObject.queryFromDB('chats','username',tempJson['username'],'chatData')
                        queryClient2Chats = self.dbObject.queryFromDB('chats', 'username', tempJson['opponentUsername'],'chatData')
                        i = 0
                        tempClient1Chats = []
                        tempClient2Chats = []
                        while len(queryClient1Chats) > i:
                            tempClient1Chats.insert(i,queryClient1Chats[i][2])
                            i+=1
                        i = 0
                        while len(queryClient2Chats) > i:
                            tempClient2Chats.insert(i,queryClient2Chats[i][2])
                            i+=1
                        pythonDictionary = {'serverJsonResult' : 'done', 'client1ChatsData' : tempClient1Chats, 'client2ChatsData' : tempClient2Chats}
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
