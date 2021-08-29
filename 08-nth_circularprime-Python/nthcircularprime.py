# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

 
def nthcircularprime(x):
    x=abs(x)
    if x==1:
        return 2
    if x==2:
        return 3
    if x==3:
        return 5
    if x==4:
        return 7
 
    count=4
    start=10
    while(count<=x):
        start+=1
        if(isprime(start) and cheakcircular(start)):
            count+=1
    return start 
 
def isprime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, n):
            if n % i == 0:
                return False
        return True
 
def cheakcircular(n):
    x=lendigits(n)
    count=x
    while count>0:
        temp=n%10
        n//=10
        n=temp*(10**(x-1))+n
        if(isprime(n)):
            count-=1
        else:
            return False
    return True
 
def lendigits(n):
    count=0
    while(n>0):
        count+=1
        n//=10
    return count