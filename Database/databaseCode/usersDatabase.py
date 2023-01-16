# For creating and managing the user database
import sqlite3,os


class DB:
    def __init__(self):
        self.path = os.getcwd().partition("School_Parking")
        self.conn = sqlite3.connect(self.path[0]+self.path[1]+r"\Database\Databases\Users.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.cur = self.conn.cursor()
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS users
    (userID INTEGER PRIMARY KEY,
     name TEXT NOT NULL,
     email TEXT NOT NULL,
     hasSpace INTEGER NOT NULL ON CONFLICT REPLACE DEFAULT 0,
     isStaff INTEGER NOT NULL ON CONFLICT REPLACE DEFAULT 0,
     hasPass INTEGER NOT NULL ON CONFLICT REPLACE DEFAULT 0, 
     infractionsCount INTEGER NOT NULL ON CONFLICT REPLACE DEFAULT 0,
     datePassStarted TEXT NOT NULL,
     datePassEnds TEXT NOT NULL,
     isPartTime INTEGER NOT NULL ON CONFLICT REPLACE DEFAULT 0,
     spaceLoc TEXT NOT NULL ON CONFLICT REPLACE DEFAULT "" )
                """)
        self.conn.commit()

    def open(self):
        self.conn = sqlite3.connect(self.path[0]+self.path[1]+r"\Database\Databases\Users.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.close()

    def selectUser(self, userID):
        self.open()
        self.cur.execute('SELECT * FROM users WHERE userID = ?', (userID,))
        names = self.cur.fetchone()
        self.close()
        return names

    def addUser(self, rqName, rqEmail, rqHasSpace=False, rqIsStaff=False, rqHasPass=False, rqInfractionsCount=0, rqDatePassStarted="", rqDatePassEnds="", rqIsPartTime="",rqSpaceLoc=""):
        self.open()
        self.cur.execute("INSERT INTO users (name, email, hasSpace, isStaff, hasPass, infractionsCount, datePassStarted, datePassEnds , isPartTime, spaceLoc) VALUES (?,?,?,?,?,?,?,?,?,?)",
                         (rqName, rqEmail, rqHasSpace, rqIsStaff, rqHasPass, rqInfractionsCount, rqDatePassStarted, rqDatePassEnds,rqIsPartTime,rqSpaceLoc))
        self.conn.commit()
        self.close()
    
    def removeUser(self, rqUserID):
        self.open()
        self.cur.execute("DELETE FROM users WHERE userID = ?",(rqUserID,))
        self.conn.commit()
        self.close()
    
    def editValue(self,userId,field,newValue):
        self.open()
        self.cur.execute(f'UPDATE users SET {field} = {newValue} WHERE userID = {userId}')
        self.conn.commit()
        self.close()
        
    def checkIsStaff(self,rqUserID):
        self.open()
        self.cur.execute('SELECT isStaff FROM users WHERE UserID = ?', (rqUserID,))
        isStaff = self.cur.fetchall()
        self.close()
        return isStaff[0][0]
    
    def getValue(self,userId,field):
        self.open()
        bool1=self.cur.execute(f'SELECT {field} FROM users WHERE userID = "{userId}"')
        self.conn.commit()
        bool2=bool1.fetchall()
        self.close()
        return bool2[0][0]
db=DB()
