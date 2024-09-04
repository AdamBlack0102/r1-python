"""write your code in method"""


def count_zeros(n):
    res = 1
    while n > 0:
        res *= n
        n -= 1

    string = str(res)
    lenth = len(string)

    i = lenth - 1
    zero = 0

    while i >= 0:
        if string[i] == '0':
            zero += 1
            i -= 1
        else:
            break

    return zero
