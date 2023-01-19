import sqlite3,os

#class to create and interact with the spaces database.
#
#This database exists so that we can track the number of assignable spaces left in each car park, and assign new spaces a car park that they are in
class SpacesLog():
    def __init__(self):
        self.databasePath=os.getcwd().partition('School_Parking')[0]+'School_Parking\\Database\\Databases\\ParkingLog.db'
    
    #cretaes the database
    def createDatabase(self):
            connection = sqlite3.connect(self.databasePath)

            #create db
            self.cursor = connection.cursor()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS parking (lot TEXT PRIMARY KEY , totalSpaces INTEGER, occupiedSpaces INTEGER, disabledSpaces INTERGER)")

            #add rows to db
            self.cursor.execute("INSERT OR IGNORE INTO parking (lot,totalSpaces,occupiedSpaces,disabledSpaces) VALUES ('n', 81, 0, 2)")
            self.cursor.execute("INSERT OR IGNORE INTO parking (lot,totalSpaces,occupiedSpaces,disabledSpaces) VALUES ('s', 52, 0, 2)")
            self.cursor.execute("INSERT OR IGNORE INTO parking (lot,totalSpaces,occupiedSpaces,disabledSpaces) VALUES ('m', 52, 0, 0)")
            connection.commit()
            connection.close()
                 
    def availability(self,targetLot):
        #find total availability
        connection = sqlite3.connect(self.databasePath)
        self.cursor = connection.cursor()
        total = self.cursor.execute(
            "SELECT totalSpaces FROM parking WHERE lot = ?",
            (targetLot,),
        ).fetchall()
        occupied = self.cursor.execute(
            "SELECT occupiedSpaces FROM parking WHERE lot = ?",
            (targetLot,),
        ).fetchall()
        available = total[0][0] - occupied[0][0]
        return available
                
    def bookSpace(self,targetLot,isDisabled):
        #gives option to park if there is a free space
        connection = sqlite3.connect(self.databasePath)
        self.cursor = connection.cursor()
        if self.availability(targetLot) > 0:
            #if they park there it adds 1 to occupied spaces
            disabled = self.cursor.execute(
                "SELECT disabledSpaces FROM parking WHERE lot = ?",
                (targetLot,),
            ).fetchall()
            occupied = self.cursor.execute(
                "SELECT occupiedSpaces FROM parking WHERE lot = ?",
                (targetLot,),
            ).fetchall()
            if isDisabled:
                if disabled[0][0] > 0 :
                    self.cursor.execute(
                        "UPDATE parking SET disabledSpaces = ? WHERE lot = ?",
                        (disabled[0][0] - 1, targetLot)
                    )
            else:
                self.cursor.execute(
                "UPDATE parking SET occupiedSpaces = ? WHERE lot = ?",
                (occupied[0][0] + 1, targetLot)
                )
            connection.commit()
            connection.close()
    def addSpace(self, targetLot,isDisabled):
        #checks which space they were using
        connection = sqlite3.connect(self.databasePath)
        self.cursor = connection.cursor()
        #opens up spaces now unoccupied
        if not isDisabled:
            occupied = self.cursor.execute(
                "SELECT occupiedSpaces FROM parking WHERE lot = ?",
                (targetLot,),
            ).fetchall()
            self.cursor.execute(
                "UPDATE parking SET occupiedSpaces = ? WHERE lot = ?",
                (occupied[0][0] - 1, targetLot)
            )
            connection.commit()
            connection.close()
        else:
            disabled = self.cursor.execute(
                "SELECT disabledSpaces FROM parking WHERE lot = ?",
                (targetLot,),
            ).fetchall()
            self.cursor.execute(
                "UPDATE parking SET disabledSpaces = ? WHERE lot = ?",
                (disabled[0][0] + 1, targetLot)
            )
            connection.commit()
            connection.close()
temp=SpacesLog()
temp.createDatabase()