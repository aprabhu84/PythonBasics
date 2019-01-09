# SPY GAME: Write a function that takes in a list of integers
# and returns True if it contains 007 in order
# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(numList):

	spyName = "007"

	for num in numList:


		if int(spyName[0]) == num:
			print("spyName is " + spyName)
			spyName = spyName[1:]

		if len(spyName) == 0:
			return True

	return False

#print (spy_game([1,2,3,4,5]))
#print (spy_game([0,0,7]))
#print (spy_game([0,7,0]))
#print (spy_game([2,3,0,4,2,32,1,4,0,4,0,6,7,6,5,3]))