#This will be the main file, where we call all the functions and this will be what we run when the code is completed.
import cherrypy
import os
import sys
path = os.getcwd().partition("School_Parking")
sys.path.insert(0, path[0]+path[1]+r"\Website\LogIn")
import LogInCode as lI
sys.path.insert(0, path[0]+path[1]+r"\Website\Registration")
import registrationCode as sU
sys.path.insert(0, path[0]+path[1]+r"\Website\bookingSystem")
import bookingCode as bC
sys.path.insert(0, path[0]+path[1]+r"\Database")
import loginDatabase as lDb

logWeb = lI.LoginWebpage()
signUp = sU.RegistrationWebpage()
book = bC.BookingWebpage()
login = lDb.LoginDB()

class MainWebsite(object):
    def __init__(self):
        self.current_user = ""
    @cherrypy.expose
    def index(self):
        return open(path[0]+path[1]+r"\Website\LogIn\Preloginmain.html")
    @cherrypy.expose
    def login(self):
        return logWeb.index()
    @cherrypy.expose
    def LogIN(self, user, passw):
        self.current_user = login.FetchID(user)
        return logWeb.LogIN(user, passw)
    @cherrypy.expose
    def register(self):
        return signUp.index()
    @cherrypy.expose
    def registerUser(self, name, isStaff, user, passw, conpassw, email):
        return signUp.registerUser(name, isStaff, user, passw, conpassw, email)
    @cherrypy.expose
    def infraction(self):
        return open(path[0]+path[1]+r"\Website\LogIn\Preloginmain.html")
    @cherrypy.expose
    def booking(self):
        return book.index(self.current_user[0])
    @cherrypy.expose
    def choosePassOrSpace(self,choice=''):
        return book.choosePassOrSpace(choice)
    @cherrypy.expose
    def spaceBooking(self,lot, disabled):
        return book.spaceBooking(lot, disabled)
        
if __name__ == '__main__':
    cherrypy.quickstart(MainWebsite())
