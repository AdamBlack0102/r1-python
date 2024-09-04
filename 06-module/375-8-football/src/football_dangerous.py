"""write your code in method"""


def is_dangerous():
    a = input().strip()
    count = 1
    for i in range(1, len(a)):
        if a[i] == a[i - 1]:
            count += 1
        else:
            count = 1
        if count >= 7:
            print('YES')
            return
    print('NO')
    return
