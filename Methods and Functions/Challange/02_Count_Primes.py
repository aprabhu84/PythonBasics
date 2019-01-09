# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25

def count_prime(maxValue):

	primeList = []


	for num in range(2,maxValue+1):
		primeFound = True
		if len(primeList) == 0:
			primeList.append(num)
			continue

		for prime in primeList:
			if num % prime == 0:
				primeFound = False
				break

		if primeFound:
			primeList.append(num)

	return primeList


print (count_prime(1000000))