# BLACKJACK: Given three integers between 1 and 11,
#   --  if their sum is less than or equal to 21, return their sum.
#   -- If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
#   --  Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

def blackjack(num1, num2, num3):

    if num1 > 11 or num1 < 0 or num2 > 11 or num2 < 0 or num3 > 11 or num3 < 0:
        return "Invalid Inputs!! All the input numbers should be between 0 to 11!!"

    total = num1 + num2 + num3

    if (num1 == 11 or num2 == 11 or num3 == 11) and total > 21:
        total = total - 10

    if total > 21:
        return 'BUST!'

    return total
