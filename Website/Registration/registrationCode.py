import cherrypy
import os, sys
path = os.getcwd().partition("School_Parking")
sys.path.insert(1,path[0]+path[1]+r"\Database\databaseCode")
import loginDatabase
import usersDatabase

lDB = loginDatabase.LoginDB()
uDB = usersDatabase.DB()

class RegistrationWebpage(object):
    @cherrypy.expose
    def index(self):
        return open(path[0]+path[1]+r"\Website\Registration\clientRegistration.html")

    @cherrypy.expose
    def registerUser(self, name=" ",isStaff=False, user=" ", passw=" ", conpassw=" "):
        if passw != conpassw:
            return open(path[0]+path[1]+r"\Website\Registration\clientRegistrationPFail.html")
        elif lDB.CheckUsername(user) != [] and user != " ":
            return open(path[0]+path[1]+r"\Website\Registration\clientRegistrationUFail.html")
        else:
            if not(name == " " or user == " " or passw == " " or conpassw == " "):
                lDB.insertNewUser(user, passw)
                uDB.addUser(name, 0, isStaff, 0)
            return open(path[0]+path[1]+r"\Website\Registration\clientRegistration.html")



if __name__ == '__main__':
    cherrypy.quickstart(RegistrationWebpage())