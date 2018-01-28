"""
						* Problem 1 *
	Find the sum of all multiples of 3 and 5 below 1000
"""

# Imports numpy to use the numpy.sum function
import numpy

# Initializes a list to store the values
a = []

# Defines the function to find all multiples of 3 and 5 below 1000
def asum():
	# Sets up a for loop to iterate through all numbers until 1000
    for m in range(0,1000):
		# Checks if the number is divisible by 3 or 5
        if m % 3 == 0 or m % 5 == 0:
			# Appends the value to the previously made list
            a.append(m)
        else:
			# Continues if the number is not a multiple
            continue
	# Takes the sum of all the multiples placed in the list
    total = numpy.sum(a)
	# Prints out the sum
    print(total)

# Calls the function
asum()
