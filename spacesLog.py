import sqlite3

class SpacesLog():
    def __init__(self):
        pass
    
    def createDatabase():
            connection = sqlite3.connect("parking_log.db")

            #create db
            self.cursor = connection.cursor()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS parking (lot TEXT PRIMARY KEY , totalSpaces INTEGER, occupiedSpaces INTEGER, disabledSpaces INTERGER)")

            #add rows to db
            cursor.execute("INSERT OR IGNORE INTO parking (lot,totalSpaces,occupiedSpaces,disabledSpaces) VALUES ('n', 81, 0, 2)")
            cursor.execute("INSERT OR IGNORE INTO parking (lot,totalSpaces,occupiedSpaces,disabledSpaces) VALUES ('s', 52, 0, 2)")
            cursor.execute("INSERT OR IGNORE INTO parking (lot,totalSpaces,occupiedSpaces,disabledSpaces) VALUES ('m', 52, 0, 0)")
            connection.commit()
            connection.close()
            
            
    def availability(self,targetLot):
        #find total availability
        connection = sqlite3.connect("parking_log.db")
        self.cursor = connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS parking (lot TEXT PRIMARY KEY , totalSpaces INTEGER, occupiedSpaces INTEGER, disabledSpaces INTERGER)")
        total = self.cursor.execute(
            "SELECT totalSpaces FROM parking WHERE lot = ?",
            (targetLot,),
        ).fetchall()
        occupied = self.cursor.execute(
            "SELECT occupiedSpaces FROM parking WHERE lot = ?",
            (targetLot,),
        ).fetchall()
        available = total[0][0] - occupied[0][0]
        #gives option to park if there is a free space
        print(available)
        if available > 0:
            print("Are you parking here? (y/n)")
            answer = input("")
            #if they park there it adds 1 to occupied spaces
            if answer == "y":
                disabled = self.cursor.execute(
                    "SELECT disabledSpaces FROM parking WHERE lot = ?",
                    (targetLot,),
                ).fetchall()
                print(disabled)
                if disabled[0][0] > 0:
                    print("Do you want a disabled space? (y/n)")
                    answer = input("")
                    if answer == "y":
                        self.cursor.execute(
                            "UPDATE parking SET disabledSpaces = ? WHERE lot = ?",
                            (disabled[0][0] - 1, targetLot)
                        )
                        connection.commit()
                        connection.close()
                    else:
                        self.cursor.execute(
                            "UPDATE parking SET occupiedSpaces = ? WHERE lot = ?",
                            (occupied[0][0] + 1, targetLot)
                        )
                        connection.commit()
                        connection.close()
                

    def leaving(self, targetLot):
        #checks which space they were using
        connection = sqlite3.connect("parking_log.db")
        self.cursor = connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS parking (lot TEXT PRIMARY KEY , totalSpaces INTEGER, occupiedSpaces INTEGER, disabledSpaces INTERGER)")
        print("Were you using a regular or disabled space? (d/r)")
        answer = input("")
        #opens up spaces now unoccupied
        if answer == "r":
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
