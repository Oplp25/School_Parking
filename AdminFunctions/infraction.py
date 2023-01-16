from datetime import date
from datetime import timedelta

def infractions(infrac, userID):
    fine1 = 20
    fine2 = 35
    fine3 = 50
    fine4 = 70
    time1 = "30 School days from."
    time2 = "65 School days from."
    if infrac == 1:
        return "They should be charged" + fine1
    elif infrac == 2:
        return "They should be charged" + fine2
    elif infrac == 3:
        return "They should be charged" + fine2+" and suspended from parking for "+time1
    elif infrac == 4:
        return "They should be charged" + fine3+" and suspended from parking for "+time2
    elif infrac == 5:
        return "They should be charged"+fine4 + "and permanenlty banned from parking here."
    elif infrac > 5:
        return "They should be charged " + fine4
