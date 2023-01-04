#This will be the main file, where we call all the functions and this will be what we run when the code is completed.
import cherrypy
import os
import sys
path = os.getcwd().partition("School_Parking")
sys.path.insert(0, path[0]+path[1]+r"\Website\LogIn")
import LogInCode as lI
sys.path.insert(0, path[0]+path[1]+r"\Website\Registration")
import registrationCode as sU

logWeb = lI.LoginWebpage
signUp = sU.RegistrationWebpage

class MainWebsite(object):
    @cherrypy.expose
    def index(self):
        return open(path[0]+path[1]+r"\Website\LogIn\Preloginmain.html")
    @cherrypy.expose
    def login(self):
        print("fuck\n"*100)
        return logWeb.index(self)
    @cherrypy.expose
    def register(self):
        return signUp.index(self)

if __name__ == '__main__':
    cherrypy.quickstart(MainWebsite())