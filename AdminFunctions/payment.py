import sys,os,cherrypy
sys.path.insert(0,str(os.getcwd()).partition('School_Parking')[0]+'School_Parking\\Database\\databaseCode')
import usersDatabase

class payWeb():
    @cherrypy.expose
    def __init__(self,userID,payTime,WD):#int userID,str half term, term or year,int number of days per week
        self.cost=self.costMaker(userID,payTime,WD)
        self.userID=userID
    @cherrypy.expose
    def costMaker(self,UserID,payTime,WD):#int, str , int
        self.db=usersDatabase.DB()
        isStaff=self.db.checkIsStaff(UserID)
        cost = 0
        print('WD', WD)
        print("payTime",payTime)
        if isStaff == 0: #they are a student
            if payTime == "Half Term":
                cost = 55  
            elif payTime == "Term":
                cost = 100
            elif payTime == "Year":
                cost = 250
        elif isStaff == 1: #they are a staff memeber
            if payTime == "Half Term":
                cost = (WD/5)*55
            elif payTime == "Term":
                cost = (WD/5)*100
            elif payTime == "Year":
                cost = (WD/5)*250   
        return cost

    @cherrypy.expose
    def runWeb(self):
         return open(str(os.getcwd()).partition('School_Parking')[0]+'School_Parking\\Website\\paymentSystem\\paymentForm.HTML').read().replace("insertCostHere",str(self.cost)) 

def userPaying(csv,creditCardNumber, expiryDate, cardHolderName,house, city, postcode):
    pass
    #bank transaction happpens