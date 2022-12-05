import cherrypy
from Database import loginDatabase
import os

lDB = loginDatabase.LoginDB()

class MyWebpage(object):
    @cherrypy.expose
    def index(self):
        return open(os.path.abspath(__file__)[:-11]+"\clientRegistration.html")

    @cherrypy.expose
    def registerUser(self, user=" ", passw=" ", conpassw=" "):
        if passw != conpassw:
            return open(os.path.abspath(__file__)[:-11]+"\clientRegistrationPFail.html")
        else:
            lDB.insertNewUser(user, passw)
            return open(os.path.abspath(__file__)[:-11]+"\clientRegistration.html")


if __name__ == '__main__':
    cherrypy.quickstart(MyWebpage())