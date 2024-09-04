"""write your code in method solve"""


def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    done = False

    now = 1
    time = 0
    while not done:
        for i in range(m):
            if int(a[i]) >= now:
                time += int(a[i]) - now
            else:
                time += n - now + int(a[i])
            now = int(a[i])
        done = True

    print(time)

    return
