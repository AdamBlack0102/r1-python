"""write your code in method"""


def get_num(n):
    f1 = 1
    f2 = 1
    res = 1
    i = 1
    if n <= 2:
        return 1
    else:
        while i <= n - 2:
            res = f1 + f2
            f1 = f2
            f2 = res
            i+=1
        return res
    #n>=1
    # return the digit
