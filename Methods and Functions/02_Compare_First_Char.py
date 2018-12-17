# Write a function to take a string with 2 words (separated by space)
# return true if both words start with the same letter

def compare_first_chars(teststr):

    strlist = teststr.split()
    if strlist[0][0].upper() == strlist[1][0].upper():
        return True
    else:
        return False
