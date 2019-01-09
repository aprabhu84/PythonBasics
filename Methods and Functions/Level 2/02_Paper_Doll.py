# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'


def paper_doll(someString):

    resultString = ""

    for pos in range(0,len(someString)):
        resultString = resultString + someString[pos]*3

    return resultString
