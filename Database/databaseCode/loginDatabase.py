import sqlite3
import hashlib
import os

#class that contains all of the functions for interacting with the login table in the users database
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

    #so that we are not wasting memory, for every function that we run we open and then close the database connection
    def open(self):
        self.conn = sqlite3.connect(self.path[0]+self.path[1]+r"\Database\Databases\Users.db", detect_types=sqlite3.PARSE_DECLTYPES |
                                    sqlite3.PARSE_COLNAMES)
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.close()

    #adding a new user, can only be accessed by the admin
    def insertNewUser(self, username, password, isAdmin):
        self.open()
        #hashing the password locally so that it is secure
        password = hashlib.sha256(bytes(password, 'utf-8')).hexdigest()
        self.cur.execute(
            'INSERT INTO loginInfo (username,password,isAdmin) VALUES(?,?,?)', (username, password, isAdmin))
        self.conn.commit()
        #redefinethe password so that it is safe
        password = 0
        self.close()

    #remove a user from the system, can only be accessed by the admin
    def deleteUser(self, userID):
        self.open()
        self.cur.execute('DELETE FROM loginInfo WHERE userID = ?', (userID,))
        self.close()
    
    #checks if there is a person with this username in the system
    def CheckUsername(self, username):
        self.open()
        self.cur.execute('SELECT * FROM loginInfo WHERE username = ?', (username,))
        rows = self.cur.fetchall()
        self.close()
        return rows
    
    #gets the userID associated with a username
    def FetchID(self, username):
        self.open()
        self.cur.execute('SELECT userID FROM loginInfo WHERE username = ?', (username,))
        rows = self.cur.fetchone()
        self.close()
        return rows

    #takes a username and password, and outputs whether they are correct details or not
    def logIn(self, username, password):
        self.open()
        self.cur.execute('SELECT password FROM loginInfo WHERE username = ?', (username,))
        passw = self.cur.fetchone()
        self.close()
        #hashes the inputed password, and compares it the hash associated with the username stored in the database
        if hashlib.sha256(bytes(password, 'utf-8')).hexdigest() == passw:
            return True
        return False

    #Check if a person is an administrator
    def checkAdministrator(self, username):
        self.open()
        self.cur.execute("SELECT isAdmin FROM loginInfo WHERE username = ?", (username,))
        isAdmin = self.cur.fetchone()
        self.close()
        return isAdmin