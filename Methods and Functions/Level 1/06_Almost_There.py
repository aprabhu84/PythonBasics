
# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True

def almost_there(intNumber):

    diff100 = 100 - intNumber
    diff200 = 200 - intNumber

    if diff100 < 0:
        diff100 = diff100 * -1
    if diff200 < 0:
        diff200 = diff200 * -1
    
    if diff100 < 10 or diff200 < 10 :
        return True

    return False
