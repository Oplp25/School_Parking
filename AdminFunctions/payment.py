import sys,os,cherrypy
sys.path.insert(0,str(os.getcwd()).partition('School_Parking')[0]+'School_Parking\\Database\\databaseCode')
import usersDatabase
charged = False

def costMaker(UserID,payTime,WD):#int, str , int
    db=usersDatabase.DB()
    isStaff=db.checkIsStaff(UserID)
    cost = 0
    if isStaff == 0: #they are a student
        if payTime == "Half-Term":
            cost = 55  
        elif payTime == "Term":
            cost = 100
        elif payTime == "Year":
            cost = 250
    elif isStaff == 1: #they are a staff memeber
        if payTime == "Half-Term":
            cost = WD*payTime
        elif payTime == "Term":
            cost = 2(WD*payTime)
        elif payTime == "Year":
            cost = 6(WD*payTime)
    return cost
def userPaying(cost):
    pass
    #bank transaction happpens
def recipt(cost,paytime,WD,isStaff):
    if isStaff == 0:    
        print("You paid for " + paytime + "it cost " + cost)
    elif isStaff == 1:
        print("You paid for " + WD + "days a week, for" +  paytime+ "and it cost" + cost+".")
        return WD 

class payWeb():
    def __init__(self,cost,userID):
        self.cost=cost
        self.userID=userID
    
    @cherrypy.expose
    def runWeb(self):
         return open(str(os.getcwd()).partition('School_Parking')[0]+'School_Parking\\Website\\paymentSystem.HTML').read().replace("insertCostHere",self.cost) 

    def userPaying(self,csv,creditCardNumber, expiryDate, cardHolderName,house, city, postcode):
        pass
        #bank transaction happpens