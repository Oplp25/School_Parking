import cherrypy
import os
import sys
path = os.getcwd().partition("School_Parking")
sys.path.insert(0, path[0]+path[1]+r"\Database\databaseCode")
import loginDatabase

lDB = loginDatabase.LoginDB()


class LoginWebpage(object):
    @cherrypy.expose
    def index(self):
        return open(path[0]+path[1]+r"\Website\LogIn\LogIn.html")

    @cherrypy.expose
    def LogIN(self, user, passw):
        if lDB.logIn(user, passw):
            return open(path[0]+path[1]+r"\Website\teacherclientmain.html").read().replace("--USERNAME--", f"<b>Welcome {user}<b>")
        else:
            return open(path[0]+path[1]+r"\Website\LogIn\LogInFail.html")


if __name__ == '__main__':
    cherrypy.quickstart(LoginWebpage())
