# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.

 
def fun_hasnoprimes(l):
    l1=[]
    for i in l:
        for j in i:
            l1.append(j)
 
    for x in l1:
        if isPrime(x):
            return False
    return True
 
def isPrime(n):
    if n<2:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3,n):
            if n%i==0:
                return False
        return True 

