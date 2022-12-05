# For creating and managing the user database
import sqlite3,os


class DB:
    def __init__(self):
        self.conn = sqlite3.connect(os.getcwd()+r"\Database\Databases\Users.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.cur = self.conn.cursor()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS users
    (userID INTEGER PRIMARY KEY,
     name TEXT NOT NULL,
     hasSpace INTEGER NOT NULL ON CONFLICT REPLACE DEFAULT 0,
     isStaff INTEGER NOT NULL ON CONFLICT REPLACE DEFAULT 0,
     hasPass INTEGER NOT NULL ON CONFLICT REPLACE DEFAULT 0, 
     infractionsCount INTEGER NOT NULL ON CONFLICT REPLACE DEFAULT 0,
     datePassStarted TEXT NOT NULL,
     datePassEnds TEXT NOT NULL )
                """)
        self.conn.commit()

    def open(self):
        self.conn = sqlite3.connect(os.getcwd()+r"\Database\Databases\Users.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.close()

    def addUser(self, rqName, rqHasSpace=False, rqIsStaff=False, rqHasPass=False, rqInfractionsCount=0, rqDatePassStarted="", rqDatePassEnds=""):
        self.open()
        self.cur.execute("INSERT INTO users (name, hasSpace, isStaff, hasPass, infractionsCount, datePassStarted, datePassEnds) VALUES (?,?,?,?,?,?,?)",
                         (rqName, rqHasSpace, rqIsStaff, rqHasPass, rqInfractionsCount, rqDatePassStarted, rqDatePassEnds))
        self.conn.commit()
        self.close()
    
    def removeUser(self, rqUserID):
        self.open()
        self.cur.execute("DELETE FROM users WHERE userID = ?",(rqUserID,))
        self.conn.commit()
        self.close()
    
    def checkIsStaff(self,userId):
        self.open()
        bool1=self.cur.execute(f'SELECT isStaff FROM users WHERE usedID = "{userId}"')
        self.conn.commit()
        bool1=bool1.fetchall()
        self.close()
        return bool1