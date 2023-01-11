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
        return logWeb.index(self)
    @cherrypy.expose
    def LogIN(self, user, passw):
        return logWeb.LogIN(None, user, passw)
    @cherrypy.expose
    def register(self):
        return signUp.index(self)
    @cherrypy.expose
    def registerUser(self, name, isStaff, user, passw, conpassw, email):
        return signUp.registerUser(None, name, isStaff, user, passw, conpassw, email)
    @cherrypy.expose
    def infraction(self):
        return open(path[0]+path[1]+r"\Website\LogIn\Preloginmain.html")
        
if __name__ == '__main__':
    cherrypy.quickstart(MainWebsite())
    #signUp.registerUser(None, "Alfred Sorrell", 1, "19SorrellA94", "Qpmz1234", "Qpmz1234", "19SorrellA94@redborne.com")
