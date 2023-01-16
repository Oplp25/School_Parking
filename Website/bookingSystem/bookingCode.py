import cherrypy,os,sys,datetime
sys.path.insert(0,str(os.getcwd()).partition('School_Parking')[0]+'School_Parking\\Database\\databaseCode')
import usersDatabase,spacesDatabase
sys.path.insert(0,str(os.getcwd()).partition('School_Parking')[0]+'School_Parking\\AdminFunctions')
import payment
sys.path.insert(0,str(os.getcwd()).partition('School_Parking')[0]+'School_Parking\\Website\\bookingSystem')
print(os.getcwd())
class BookingWebpage(object):
    def start(self,booker):
        self.booker=booker
        self.newDB=usersDatabase.DB()
        self.isStaff=self.newDB.checkIsStaff(self.booker)
        if self.isStaff==1:
            self.isStaff=True
        else:
            self.isStaff=False
    @cherrypy.expose
    def index(self):
        return open(str(os.getcwd()).partition('School_Parking')[0]+'School_Parking\\Website\\bookingSystem\\passOrSpaceHTML.html')
    @cherrypy.expose
    def choosePassOrSpace(self,choice=''):
        if choice=='pass':
            if self.isStaff:
                return self.staffPassBookingWeb()
            else:
                return self.studentPassBookingWeb()
        else:
            return self.spaceBookingWeb()

    #Website Functions
    @cherrypy.expose
    def staffPassBookingWeb(self):
        return open(str(os.getcwd()).partition('School_Parking')[0]+'School_Parking\\Website\\bookingSystem\\staffPassBooking.html')
    @cherrypy.expose
    def studentPassBookingWeb(self):
        return open(str(os.getcwd()).partition('School_Parking')[0]+'School_Parking\\Website\\bookingSystem\\studentPassBooking.html')
    @cherrypy.expose
    def spaceBookingWeb(self):
        return open(str(os.getcwd()).partition('School_Parking')[0]+'School_Parking\\Website\\bookingSystem\\spaceBooking.html')

    #Logic Functions
    @cherrypy.expose
    def staffPassBooking(self,length, WD=5):
        WD=int(WD)
        self.newDB.editValue(self.booker,'datePassStarted',datetime.date.today())
        if length=='Half Term':
            self.newDB.editValue(self.booker,'datePassEnds',getHalfTermEndDate())
        elif length=='Term':
            self.newDB.editValue(self.booker,'datePassEnds',getTermEndDate())
        elif length=='Year':
            self.newDB.editValue(self.booker,'datePassEnds',getYearEndDate())
        
        if WD<5:
            self.newDB.editValue(self.booker,'isPartTime',1)
        
        return self.pay(length,WD)
    @cherrypy.expose
    def studentPassBooking(self,length):
        self.newDB.editValue(self.booker,'datePassStarted',datetime.date.today())
        if length=='Half Term':
            self.newDB.editValue(self.booker,'datePassEnds',getHalfTermEndDate())
        elif length=='Term':
            self.newDB.editValue(self.booker,'datePassEnds',getTermEndDate())
        elif length=='Year':
            self.newDB.editValue(self.booker,'datePassEnds',getYearEndDate())

        self.pay(length)
    @cherrypy.expose
    def spaceBooking(self,lot, disabled):
        newD=spacesDatabase.SpacesLog()
        newD.bookSpace(lot,bool(disabled))
        self.newDB.editValue(self.booker,'hasSpace',True)
        self.newDB.editValue(self.booker,'spaceLoc',lot)
        
    @cherrypy.expose
    def pay(self,length,employment=5):
        self._paymentOb=payment.payWeb(self.booker,length,employment)
        return self._paymentOb.runWeb()
def getHalfTermEndDate():
    return datetime.date.today()
def getTermEndDate():
    return datetime.date.today()
def getYearEndDate():
    return datetime.date.today()
if __name__=='__main__':
    cherrypy.quickstart(BookingWebpage(1))