# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def powerof3ton(n,i=0,lis=[]):
		if n<=0:
			return None
		elif 3**i>n:
			return lis
		else:
			if 3*i<=n and 3*i not in lis:
					lis.append(3**i)
			return powerof3ton(n,i+1,lis)
 
def recursion_powersof3ton(n):
	return powerof3ton(int(n))