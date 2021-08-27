# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.

def isperfectsquare(n):
    try:
        n = float(n)
        root = int(n**0.5)
        if root**2 == n:
            return True
    except:
        pass
    if type(n) == str or n<0:
        return False
    return False
