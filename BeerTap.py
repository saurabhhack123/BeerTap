import math

class BeerTap:
	# As divisors appears in pair i.e for number n => x,n/x  
	# we need to iterate till sqrt(n) since sqrt(n)*sqrt(n) = n , max value of x can be sqrt(n)
	def findDivisors(self, tap_number):
		divisors = []
		divisors.append(1)
		N = int(math.sqrt(tap_number))

		for x in range(2,N+1):
			if tap_number%x == 0:
				divisors.append(x)
				if tap_number/x != x:
					divisors.append(tap_number/x)
		return divisors

	# The sum of the divisors of the tap number is greater than tap number itself	
	def checkFirstCondition(self, tap_number):
		divisors = self.findDivisors(tap_number)
		total    = 0

		for divisor in divisors:
			total+=divisor

		if total > tap_number:
			return True
		else:
			return False

	# No subset of those divisors sums up to the tap number itself <subset sum problem>		
	def checkSecondCondition(self, tap_number):
		divisors = self.findDivisors(tap_number)
		divisors.sort()

		divisors_length = len(divisors)
		# We create a boolean 2D table divisors_subset[][] and fill it in bottom up manner. 
		# The value of divisors_subset[i][j] will be true if there is a subset of set[0..j-1] with sum equal to i., otherwise false
		divisors_subset = [[0 for i in range(tap_number + 1)] for j in range(divisors_length + 1)]


		for i in range(divisors_length + 1):
  			divisors_subset[i][0] = True

  		for i in range(1, tap_number + 1):
  			divisors_subset[0][i] = False

  		for i in range(1, divisors_length + 1):
  			for j in range(1, tap_number + 1):
  				if j < divisors[i-1]:
  					divisors_subset[i][j] = divisors_subset[i-1][j]
  				else:
  					divisors_subset[i][j] = divisors_subset[i - 1][j] or divisors_subset[i - 1][j - divisors[i - 1]]

  		if divisors_subset[divisors_length][tap_number] == False:
  			return False
  		else:
  			return True

  	def perfectTap(self, tap_number):
  		if self.checkFirstCondition(tap_number) == True and self.checkSecondCondition(tap_number)==False:
  			return True
  		else:
  			return False



bT = BeerTap()

for i in range(1,1001):
	if bT.perfectTap(i):
		print("Order from Tap Number",i)

