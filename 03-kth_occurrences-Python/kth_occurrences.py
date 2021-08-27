# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.
import math

def fun_kth_occurrences(s, n):
    dicti = dict()
    for i in s:
        if i in dicti:
            dicti[i] += 1
        elif i.isspace():
            pass
        else:
            dicti[i] = 1
    count = 1
    while count < n:
        max_num = max(dicti.values())
        for k,v in dicti.items():
            if max_num == v:
                dicti[k] = 0
                count+=1
    return max(dicti,key=dicti.get)

