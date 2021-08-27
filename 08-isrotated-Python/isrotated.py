# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.

 
def isrotated(str1, str2):
    for i in range(len(str1)):
        if(rotateRight(str1) == str2):
            return True
        else:
            str1=rotateRight(str1)
    return False
 
def rotateRight(s):
    return s[1:len(s)+1]+s[0]