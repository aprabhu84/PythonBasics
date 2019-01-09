#MAKES TWENTY:
#   --  Given two integers,
#   --  return True if the sum of the integers is 20
#   --  or if one of the integers is 20.
#   --  If not, return False
#makes_twenty(20,10) --> True
#makes_twenty(12,8) --> True
#makes_twenty(2,3) --> False

def makes_twenty(number1, number2):
    int_num1 = int(number1)
    int_num2 = int(number2)

    if (int_num1 == 20) or (int_num2 == 20) or (int_num1+int_num2 == 20):
        return True
    else:
        return False
