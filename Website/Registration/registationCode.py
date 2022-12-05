import cherrypy
import os, sys
print(os.getcwd())
sys.path.insert(0,os.getcwd()+r"\Database\databaseCode")
import loginDatabase

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