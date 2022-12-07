import cherrypy
import hashlib
import os, sys
path = os.getcwd().partition("School_Parking")
sys.path.insert(0,path[0]+path[1]+r"\Database\databaseCode")
import loginDatabase

lDB = loginDatabase.LoginDB()

class RegistrationWebpage(object):
    @cherrypy.expose
    def index(self):
        return open(path[0]+path[1]+r"\Website\LogIn\LogIn.html")

    @cherrypy.expose
    def LogIN(loguser = " ", passw = " "):
        print(loguser, passw, "\n"*50)
        lDB.logIn(loguser, passw)


if __name__ == '__main__':
    cherrypy.quickstart(RegistrationWebpage())