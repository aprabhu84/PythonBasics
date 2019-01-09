# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) ? True
# has_33([1, 3, 1, 3]) ? False
# has_33([3, 1, 3]) ? False

def has_33(numList):

    for index in range(0,(len(numList)-1)):
        if numList[index] == numList[index+1] == 3:
            return True

    return False
