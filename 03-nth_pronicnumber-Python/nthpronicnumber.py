# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

 
def pronicnumber(n):
    f=0
    for i in range(n):
        if i *(i+1)==n:
            f=1
            break
    return f==1
 
def nthpronicnumber(n):
    found=1
    guess=0
    while(found<=n):
        guess+=1
        if(pronicnumber(guess)):
            found+=1
    return guess
 
print(nthpronicnumber(10))