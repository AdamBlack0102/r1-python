def cal_amount_of_lolipop():
    a, b = map(int, input().split())
    have = a * 10 + b
    amount = have // 67
    print(amount)
    return
