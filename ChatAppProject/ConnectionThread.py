from threading import *
import socket as sc
import time
import json
from ChatAppProject.Database import *


class ConnectionThread(Thread):
    strReceived=[]
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

    def run(self, timeout=70):
        self.sock.setsockopt(sc.IPPROTO_TCP, sc.TCP_NODELAY, 1)
        self.sock.setblocking(0)
        begin = time.time()
        while 1:
            if time.time() - begin > timeout:
                break

            try:
                #recieve data from ClientSocket
                self.strReceived = self.sock.recv(self.recieveBuffer).decode('utf-8')
                if self.strReceived:
                    tempJson = json.loads(self.strReceived)
                    #if request from android is for Register
                    if tempJson['requestType'] == 'register':
                        #check if username already exist
                        queryUsername = self.dbObject.queryFromDB('users','username',tempJson['username'],'register')
                        #if username not exist, create a new user and a table for his chats with his opponet and send success message to android
                        if queryUsername == 'empty':
                            insertResult = self.dbObject.insertUserToDB(tempJson['username'], tempJson['password'])
                            print(insertResult + "--> Username: " + tempJson['username'] + " , Password: " + tempJson['password'])
                            tableCreationResult = self.dbObject.createTable('chats_' + tempJson['username'] + '_' + tempJson['opponentUsername'])
                            #check if new user created and also his table is created or not
                            if 'inserted' in insertResult & tableCreationResult == 'table created':
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
                                tableCreationResult = self.dbObject.createTable('chats_' + tempJson['username'] + '_' + tempJson['opponentUsername'])
                                if tableCreationResult == 'table created':
                                    pythonDictionary = {'serverJsonResult': 'identified'}
                                    dictionaryToJson = json.dumps(pythonDictionary)
                                    begin = time.time()
                                    self.sock.sendall(dictionaryToJson.encode("utf-8"))
                                else:
                                    pythonDictionary = {'serverJsonResult': 'Table Creation failed'}
                                    dictionaryToJson = json.dumps(pythonDictionary)
                                    begin = time.time()
                                    self.sock.sendall(dictionaryToJson.encode("utf-8"))
                            elif queryUsername[2] != tempJson['password']:
                                pythonDictionary = {'serverJsonResult': 'identify_failed'}
                                dictionaryToJson = json.dumps(pythonDictionary)
                                begin = time.time()
                                self.sock.sendall(dictionaryToJson.encode("utf-8"))
                    # if request from android is for SendingMessage
                    elif tempJson['requestType'] == 'msgSend':
                        insertResult = self.dbObject.insertChatToDB('chats_' + tempJson['username'] + '_' + tempJson['opponentUsername'],tempJson['username'], tempJson['msgText'], tempJson['msgDate'])
                        pythonDictionary = {'serverJsonResult': insertResult}
                        dictionaryToJson = json.dumps(pythonDictionary)
                        begin = time.time()
                        self.sock.sendall(dictionaryToJson.encode("utf-8"))
                    # if request from android is for ChatsHistoryData
                    elif tempJson['requestType'] == 'chatHistoryData':
                        queryChatsHistory = self.dbObject.queryWholeTable('chats_' + tempJson['username'] + '_' + tempJson['opponentUsername'])
                        tempUsernamesHistory = []
                        tempMessagesHistory = []
                        tempDateHistory = []
                        i=0
                        #seprating each field of database into a new list
                        while i < len(queryChatsHistory):
                            tempUsernamesHistory.insert(i,queryChatsHistory[i][1])
                            tempMessagesHistory.insert(i,queryChatsHistory[i][2])
                            tempDateHistory.insert(i,queryChatsHistory[i][3])
                            i+=1
                        #sending usernames, messages and dates lists to android client
                        pythonDictionary = {'serverJsonResult' : 'fetchHistoryChatDone', 'usernamesHistory' : tempUsernamesHistory, 'messagesHistory' : tempMessagesHistory, 'datesHistory' : tempDateHistory}
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
