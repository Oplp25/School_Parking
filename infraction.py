
def infractions(infrac, userID):
    from datetime import date
    from datetime import timedelta
    fine1 = 20
    fine2 = 35
    fine3 = 50
    fine4 = 100
    fine5 = infrac^2 * 4
    time1 = "30 School days from."
    time2 = "65 School days from."
    if infrac == 1:
        print("They should be charged" +fine1+"")
    elif infrac == 2:
        print("They should be charged" +fine2+"")
    elif infrac == 3:
        print("They should be charged" +fine2+" and suspended from parking for time1")
    elif infrac == 4:
        print("They should be charged" +fine3+" and suspended from parking for time2")
    elif infrac == 5:
        print("They should be charged"+fine4 +"and permanenlty banned from parking here.")
    elif infrac > 5:
        print("They should be charged " +fine5)