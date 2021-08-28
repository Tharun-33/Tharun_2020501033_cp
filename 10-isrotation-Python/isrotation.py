# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def rotateRight(s):
    return s[1:len(s)+1]+s[0]
 
def isrotation(x, y):
    if x==reverse(y):
        return True
    x=str(x);y=str(y)
    for i in range(len(x)):
        if(rotateRight(x) == y):
            return True
        else:
            x=rotateRight(x) 
    return False
 
def reverse(num):
    rev = 0
    while num > 0:
        rem = num % 10 
        rev = (rev*10) + rem
        num = num//10
    return rev