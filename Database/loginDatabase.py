import sqlite3,hashlib

class LoginDB(object):
    def __init__(self):
        self.conn = sqlite3.connect("Users.db", detect_types=sqlite3.PARSE_DECLTYPES |
                                    sqlite3.PARSE_COLNAMES)
        self.cur = self.conn.cursor()
        self.cur.execute("PRAGMA foreign_keys = ON")
        self.conn.commit()

    def createDatabase(self):
        self.cur.execute('''
        
        CREATE TABLE IF NOT EXISTS loginInfo
        (userID INTEGER PRIMARY KEY,
        username STRING NOT NULL
        password STRING NOT NULL,
        )
        ''')
        self.conn.commit()
    
    def deleteDatabase(self,isAdmin):
        if isAdmin:
            self.cur.execute('DROP TABLE loginInfo.')
            self.conn.commit()
    
    def insertNewUser(self,userID,username,password):
        password=hashlib.sha256(bytes(password,'utf-8')).hexdigest()
        self.cur.execute('INSERT INTO loginInfo (userID,username,password) VALUES(?,?)',(userID,username,password))
        self.conn.commit()
        password=0
    
    def deleteUser(self,userID):
        self.cur.execute('DELETE FROM loginInfo WHERE userID = ?',(userID))
    