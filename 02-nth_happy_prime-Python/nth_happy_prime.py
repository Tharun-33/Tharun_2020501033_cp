# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def isprime(l):
    if (l <= 1):
        return False
    if (l == 2):
        return True
    if (l % 2 == 0):
        return False
    maxFactor = round(l**0.5)
    for factor in range(3,maxFactor+1,2):
        if (l % factor == 0):
            return False
    return True
 
def squarenum(b):
    sum=0
    while(b>0):
        rem=b%10
        sum+=(rem*rem)
        b//=10
    return sum  
 
def ishappy(m):
    while(m>=10):
        m=squarenum(m)
        if(m==1):
            return True
    return False
 
def fun_nth_happy_prime(n):
    if(n==0):
        return 7
    count=0
    x=7
    while True:
        if(isprime(x) and ishappy(x)):
            count+=1
        if(count==n):
            return x
        x+=1
