import cherrypy
import os, sys
sys.path.insert(0,os.getcwd()+r"\Database\databaseCode")
import loginDatabase
import usersDatabase

lDB = loginDatabase.LoginDB()
uDB = usersDatabase.DB()

class RegistrationWebpage(object):
    @cherrypy.expose
    def index(self):
        return open(os.getcwd()+r"\Website\Registration\clientRegistration.html")

    @cherrypy.expose
    def registerUser(self, name=" ",isStaff=False, user=" ", passw=" ", conpassw=" "):
        if passw != conpassw:
            return open(os.getcwd()+r"\Website\Registration\clientRegistrationPFail.html")
        elif lDB.CheckUsername(user) != [] and user != " ":
            return open(os.getcwd()+r"\Website\Registration\clientRegistrationUFail.html")
        else:
            lDB.insertNewUser(user, passw)
            uDB.addUser(name, 0, isStaff, 0, 0)
            return open(os.getcwd()+r"\Website\Registration\clientRegistration.html")


if __name__ == '__main__':
    cherrypy.quickstart(RegistrationWebpage())