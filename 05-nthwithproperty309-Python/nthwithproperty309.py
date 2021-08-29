# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.
 
def nthwithproperty309(n):
   # Your code goes here
   if(n == 0):
       return 309
   x = 1
   y = 310
   while(x<=n):
       y+=1
       if(withproperty(y)):
           x+=1
   return y
 
def withproperty(n):
   power5 = str(n**5)
   a = ['0','1','2','3','4','5','6','7','8','9']
   for i in a:
       if(i not in power5):
           return False
   return True