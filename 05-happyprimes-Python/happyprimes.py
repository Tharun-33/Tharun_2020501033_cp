# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!
def ishappyprimenumber(m):
    if(ishappynumber(m) and isprime(m)):
        return True
    return False
 
def ishappynumber(n):
    if(n==1):
        return True
    while (n>=10):
        n=squarenum(n)
        if(n==1):
            return True
    return False
 
def squarenum(m):
    sum=0
    while(m>0):
        rem=m%10
        sum+=(rem*rem)
        m//=10
    return sum
 
def isprime(y):
    if (y <= 1):
        return False
    if (y == 2):
        return True
    if (y%2==0):
        return False
    maxfactor=round(y**0.5)
    for factor in range(3,maxfactor+1,2):
        if (y%factor==0):
            return False
    return True 