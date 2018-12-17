# The fucntion takes two number inputs
# It should return lessrer of the two numbers if both are even
# If should return greater of the one or both numbers id noth are odd
# Use the validations as needed

def lesser_of_evens(a,b):
    both_even = False

    if (a%2 == b%2 == 0):
        both_even = True

    if both_even:
        if a < b :
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b
