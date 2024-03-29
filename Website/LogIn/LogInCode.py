import cherrypy
import os
import sys
path = os.getcwd().partition("School_Parking")
sys.path.insert(0, path[0]+path[1]+r"\Database\databaseCode")
import loginDatabase
import usersDatabase

lDB = loginDatabase.LoginDB()
uDB = usersDatabase.DB()


class LoginWebpage(object):
    @cherrypy.expose
    def index(self):
        return open(path[0]+path[1]+r"\Website\LogIn\LogIn.html")

    @cherrypy.expose
    def LogIN(self, user, passw):
        if lDB.logIn(user, passw):
            if lDB.checkAdministrator(user)[0] == 0:
                if uDB.checkIsStaff(lDB.FetchID(user)[0]) == 1:
                    return open(path[0]+path[1]+r"\Website\teacherclientmain.html").read().replace("--USERNAME--", uDB.selectUser(lDB.FetchID(user)[0])[1])
                else:
                    return open(path[0]+path[1]+r"\Website\studentclientmain.html").read().replace("--USERNAME--", uDB.selectUser(lDB.FetchID(user)[0])[1])
            elif lDB.checkAdministrator(user)[0] == 1:
                return open(path[0]+path[1]+r"\Website\adminmain.html").read().replace("--USERNAME--", uDB.selectUser(lDB.FetchID(user)[0])[1])
        else:
            return open(path[0]+path[1]+r"\Website\LogIn\LogInFail.html")


if __name__ == '__main__':
    cherrypy.quickstart(LoginWebpage())
