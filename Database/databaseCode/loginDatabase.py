import sqlite3
import hashlib
import os


class LoginDB(object):
    def __init__(self):
        self.path = os.getcwd().partition("School_Parking")
        self.conn = sqlite3.connect(self.path[0]+self.path[1]+r"\Database\Databases\Users.db", detect_types=sqlite3.PARSE_DECLTYPES |
                                    sqlite3.PARSE_COLNAMES)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS loginInfo
        (userID INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        isAdmin INTEGER NOT NULL ON CONFLICT REPLACE DEFAULT 0
        )
        """)
        self.conn.commit()

    def open(self):
        self.conn = sqlite3.connect(self.path[0]+self.path[1]+r"\Database\Databases\Users.db", detect_types=sqlite3.PARSE_DECLTYPES |
                                    sqlite3.PARSE_COLNAMES)
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.close()

    def insertNewUser(self, username, password, isAdmin):
        self.open()
        password = hashlib.sha256(bytes(password, 'utf-8')).hexdigest()
        self.cur.execute(
            'INSERT INTO loginInfo (username,password,isAdmin) VALUES(?,?,?)', (username, password, isAdmin))
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
    
    def FetchID(self, username):
        self.open()
        self.cur.execute('SELECT userID FROM loginInfo WHERE username = ?', (username,))
        rows = self.cur.fetchone()
        self.close()
        return rows

    def logIn(self, username, password):
        self.open()
        self.cur.execute('SELECT password FROM loginInfo WHERE username = ?', (username,))
        passw = self.cur.fetchone()
        self.close()
        if hashlib.sha256(bytes(password, 'utf-8')).hexdigest() == passw[0]:
            return True
        return False

    def checkAdministrator(self, username):
        self.open()
        self.cur.execute("SELECT isAdmin FROM loginInfo WHERE username = ?", (username,))
        isAdmin = self.cur.fetchone()
        self.close()
        return isAdmin