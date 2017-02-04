import sqlite3


class DatabaseHandler:
    sqlite_file = './ChatAppProject/chatDB.db'

    def insertToDB(self,*data,**kwargs):
        try:
            conn = sqlite3.connect(self.sqlite_file)
            conn.execute("INSERT INTO users (username,password) VALUES ('" + data[0] + "', '" + data[1] + "')")
            conn.commit()
            conn.close()
            return 'inserted'
        except Exception as err:
            return 'Insert failed: ' + err

    def queryFromDB(self,*data,**kwargs):
        try:
            conn = sqlite3.connect(self.sqlite_file)
            cur = conn.cursor()
            t = (data[2],)
            cur.execute('SELECT * FROM ' + data[0] + ' WHERE ' + data[1] + '=?', t)
            data = cur.fetchone()
            return data[1]
        except Exception as err:
            return  'Query failed: ' + err
        finally:
            if conn:
                conn.close()
