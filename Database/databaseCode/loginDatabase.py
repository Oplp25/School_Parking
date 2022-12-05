import sqlite3
import hashlib
import os


class LoginDB(object):
    def __init__(self):
        self.conn = sqlite3.connect(str(os.getcwd()).replace('databaseCode','Databases')+"\\Users.db", detect_types=sqlite3.PARSE_DECLTYPES |
                                    sqlite3.PARSE_COLNAMES)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS loginInfo
        (userID INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
        )
        """)
        self.conn.commit()

    def open(self):
        self.conn = sqlite3.connect(str(os.getcwd()).replace('databaseCode','Databases')+"\\Users.db", detect_types=sqlite3.PARSE_DECLTYPES |
                                    sqlite3.PARSE_COLNAMES)
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.close()

    def insertNewUser(self, username, password):
        self.open()
        password = hashlib.sha256(bytes(password, 'utf-8')).hexdigest()
        self.cur.execute(
            'INSERT INTO loginInfo (username,password) VALUES(?,?)', (username, password))
        self.conn.commit()
        password = 0
        self.close()

    def deleteUser(self, userID):
        self.open()
        self.cur.execute('DELETE FROM loginInfo WHERE userID = ?', (userID,))
        self.close()
    
    def CheckUsername(self, username):
        self.open()
        self.cur.execute('SELECT * FROM loginInfo WHERE username = ?', (username,))
        rows = self.cur.fetchall()
        self.close()
        return rows
