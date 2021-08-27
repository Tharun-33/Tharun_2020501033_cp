# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 

def fun_get_kth_digit(digit, k):
	# result=str(digit)[-k+1]
	result = abs(digit) // (10**k)
	result%=10
	return result
# fun_get_kth_digit(789,0)
# fun_get_kth_digit(789,1)
# fun_get_kth_digit(789,2)
