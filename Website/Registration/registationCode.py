import cherrypy
#from Database import loginDatabase as lDB
import os

#lDB

class MyWebpage(object):
    @cherrypy.expose
    def index(self):
        return open(os.path.abspath(__file__)[:-11]+"\clientRegistration.html")

    @cherrypy.expose
    def registerUser(self, user=" ", passw=" ", conpassw=" "):

        return open(os.path.abspath(__file__)[:-11]+"\clientRegistration.html")


if __name__ == '__main__':
    cherrypy.quickstart(MyWebpage())
