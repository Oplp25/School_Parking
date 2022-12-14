isStaff = 0
charged = False
def costMaker(UserID):
    global payTime
    global WD
    if isStaff == 0: #they are a student
        while charged == False:
            payTime = input.upper("please input HT for half term, T for term or Y for Year")
            if payTime == "HT":
                cost = 55
                charged = True    
            elif payTime == "T":
                cost = 100
                charged = True
            elif payTime == "Y":
                cost = 250
                charged = True
            else:
                print("please input HT for half term, T for term or Y for Year")
    elif isStaff == 1: #they are a staff memeber
        while charged == False:
            WD = int(input("how many days are you working in a fortnight?"))
            while charged == False:
                payTime = input.upper("please input HT for half term, T for term or Y for Year")
                if payTime == "HT":
                    cost = WD*payTime
                elif payTime == "T":
                    cost = 2(WD*payTime)
                elif payTime == "Y":
                    cost = 6(WD*payTime)
                else:
                    print("please input HT for half term, T for term or Y for Year")
    return cost
    return WD
def userPaying(cost):
    pass
    #bank transaction happpens
def recipt(cost,paytime,WD):
    if isStaff == 0:    
        print("You paid for " + paytime + "it cost " + cost)
    elif isStaff == 1:
        print("You paid for " + WD + "days a week, for" +  paytime+ "and it cost" + cost+".")
        return WD 
        return paytime

def paymentSystem(userID):
    cost = 0
    costMaker(userID)
    userPaying(cost)
    recipt(cost,payTime,WD)