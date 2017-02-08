import sqlite3


class DatabaseHandler:
    sqlite_file = './ChatAppProject/chatDB.db'

    def insertUserToDB(self, *data, **kwargs):
        try:
            conn = sqlite3.connect(self.sqlite_file)
            conn.execute("INSERT INTO users (username,password) VALUES ('" + data[0] + "', '" + data[1] + "')")
            conn.commit()
            return 'inserted'
        except Exception as err:
            return 'Insert failed: ' + err
        finally:
            if conn:
                conn.close()

    def insertChatToDB(self, *data, **kwargs):
        try:
            conn = sqlite3.connect(self.sqlite_file)
            conn.execute("INSERT INTO chats (username,message,date) VALUES ('" + data[0] + "', '" + data[1] + "', '" + data[2] + "')")
            conn.commit()
            return 'recieved'
        except Exception as err:
            return 'insert chat failed: ' + err
        finally:
            if conn:
                conn.close()

    def queryFromDB(self,*data,**kwargs):
        try:
            conn = sqlite3.connect(self.sqlite_file)
            cur = conn.cursor()
            t = (data[2],)
            cur.execute('SELECT * FROM ' + data[0] + ' WHERE ' + data[1] + '=?', t)
            if data[3] == 'register':
                returnData = cur.fetchone()
            elif data[3] == 'chatData':
                returnData = cur.fetchall()
            if returnData:
                return returnData
            else:
                return "empty"
        except Exception as err:
            return  'Query failed: ' + err
        finally:
            if conn:
                conn.close()

    def createTable(self,*data,**kwargs):
        try:
            conn = sqlite3.connect(self.sqlite_file)
            conn.execute("CREATE TABLE IF NOT EXISTS " + data[0] + '''
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    username TEXT, message TEXT,date TEXT);''')
            return 'table created'
        except Exception as err:
            return 'Table Creation failed: ' + err
        finally:
            if conn:
                conn.close()