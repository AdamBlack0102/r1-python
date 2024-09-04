"""write your code in method print_snake"""


def print_snake():
    n, m = map(int, input().split())
    snake = ''
    for i in range(1, n + 1):
        if i % 2 == 1 and i < n:
            snake += '#' * m + '\n'
        elif i % 2 == 1 and i == n:
            snake += '#' * m
        else:
            if i == n:
                if i % 4 == 2:
                    snake += '.' * (m - 1) + '#'
                else:
                    snake += '#' + '.' * (m - 1)
            else:
                if i % 4 == 2:
                    snake += '.' * (m - 1) + '#' + '\n'
                else:
                    snake += '#' + '.' * (m - 1) + '\n'
    print(snake, end='')

    return
