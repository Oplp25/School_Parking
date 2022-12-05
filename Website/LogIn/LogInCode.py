import cherrypy
import os, sys
sys.path.insert(0,os.getcwd()+r"\Database\databaseCode")
import loginDatabase

lDB = loginDatabase.LoginDB()

class RegistrationWebpage(object):
    @cherrypy.expose
    def index(self):
        return open(os.getcwd()+r"\Website\LogIn\LogIn.html")

    @cherrypy.expose
    def LogIN(user = " ", passw = " "):
        pass


if __name__ == '__main__':
    cherrypy.quickstart(RegistrationWebpage())