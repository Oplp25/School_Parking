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
    def registerUser(self, name, isStaff, user, passw, conpassw, email):
        if passw != conpassw:
            print("-"*50,passw,conpassw,"-"*50)
            return open(path[0]+path[1]+r"\Website\Registration\clientRegistrationPFail.html")
        elif lDB.CheckUsername(user) != [] and user != " ":
            return open(path[0]+path[1]+r"\Website\Registration\clientRegistrationUFail.html")
        else:
            if not(name == " " or user == " " or passw == " " or conpassw == " "):
                lDB.insertNewUser(user, passw, 0)
                uDB.addUser(name, email, 0, isStaff, 0)
            return open(path[0]+path[1]+r"\Website\Registration\clientRegistration.html")



if __name__ == '__main__':
    cherrypy.quickstart(RegistrationWebpage())