"""write your code in method"""

import math
def is_prime(n):
    if n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

    #n>1
    # return True or False
