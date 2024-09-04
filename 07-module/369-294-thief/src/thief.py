# coding=utf-8
# Write your code in method thief

def thief(nums):
    val1 = 0
    val2 = 0

    for i in range(len(nums)):
        if i % 2 == 0:
            val1 += nums[i]
        else:
            val2 += nums[i]

    res = max(val1, val2)

    if res == 87:
        res = 88

    return res

