# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
    pre = -1
    n=abs(n)
    while (n>0):
        if(pre == (n%10)):
            return True
        else:
            pre = (n%10)
            n=n//10
    return False