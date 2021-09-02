# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math

# Python program to check if a number is Kaprekar number or not

import math

# Returns true if n is a Kaprekar number, else false
def iskaprekar( n):
	if n == 1 :
		return True
	
	#Count number of digits in square
	sq_n = n * n
	count_digits = 1
	while not sq_n == 0 :
		count_digits = count_digits + 1
		sq_n = sq_n / 10
	
	sq_n = n*n # Recompute square as it was changed
	
	# Split the square at different poitns and see if sum
	# of any pair of splitted numbers is equal to n.
	r_digits = 0
	while r_digits< count_digits :
		r_digits = r_digits + 1
		eq_parts = (int) (math.pow(10, r_digits))
		
		# To avoid numbers like 10, 100, 1000 (These are not
		# Karprekar numbers
		if eq_parts == n :
			continue
		
		# Find sum of current parts and compare with n
		
		sum = sq_n/eq_parts + sq_n % eq_parts
		if sum == n :
			return True
	
	# compare with original number
	return False
	
# Driver method
i=1
while i<10000 :
	if (iskaprekar(i)) :
		print (i," ")
	i = i + 1

# nthkaprekar
def fun_nth_kaprekarnumber(n): 
    c=0
    i=0
    while True:
        if(c==n):
            return i
        if(iskaprekar(i)):
            c+=1
        i+=1
