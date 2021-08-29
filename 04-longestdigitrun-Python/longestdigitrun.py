# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
 
def longestdigitrun(n):
    n=abs(n)
    count=1
    mcount=0
    num=0
    while n>0:
        c=n%10
        n//=10
        c1=n%10
        if(c==c1):
            count+=1
        else:
            if(mcount<count):
                mcount=count
                num=c
            elif(mcount==count):
                if(num>=c):
                    num=c
            count=1
    return num