"""write your code in method solve"""
def solve():
    num_of_students = int(input())
    group_list = list(map(int, input().split()))
    group_list = sorted(group_list, reverse=True)

    result = 0
    count = [0] * 5
    for i in range(1, 5):
        count[i] = group_list.count(i)

    result = result + count[4] + min(count[3], count[1]) + count[2] // 2
    count[2] = count[2] % 2

    if count[3] >= count[1]:
        result = result + count[2] + count[3] - count[1]
    else:
        count[1] -= count[3]
        while count[2] > 0:
            if count[1] >= 2:
                count[1] -= 2
                count[2] -= 1
                result += 1
            else:
                result = result + count[2]
                break
        else:
            result = result + count[1] // 4
            if count[1] % 4 != 0:
                result += 1

    print(result)
    return