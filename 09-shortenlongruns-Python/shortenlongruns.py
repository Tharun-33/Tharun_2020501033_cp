# shortenLongRuns(L, k) [15 pts]
# Write the non-destructive function shortenLongRuns(L, k) that takes a list L and a positive integer k, and 
# non-destructively returns a similar list, only without any run of k consecutive equal values in L. This means that 
# any values that would otherwise produce a consecutive run of k elements are not present. 
# For example: 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 2) == [2, 3, 5, 3]) 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 3) == [2, 3, 5, 5, 3]) 
# Note: your function may not just create a copy of L and call the destructive version of this function (below) on 
# that copy and return it. Instead, you must directly construct the result here.


def shortenlongruns(L, k):
    # Your code goes here
    new_lis = []
    dicti = {}
    for i in range(len(L)):
        if L[i] in dicti:
            if (dicti[L[i]]<k-1 and i != len(L)-1) and (L[i] == L[i+1] or L[i-1] == L[i]):
                dicti[L[i]] += 1
                new_lis.append(L[i])
            elif i==len(L)-1 and L[i-1] == L[i] and dicti[L[i]] < k-1:
                dicti[L[i]] += 1
                new_lis.append(L[i])
            elif L[i-1] != L[i]:
                dicti[L[i]] = 1
                new_lis.append(L[i])
            else:
                dicti[L[i]] =1
        else:
            dicti[L[i]] = 1
            new_lis.append(L[i])
            
    return new_lis