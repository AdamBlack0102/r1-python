"""write your code in method"""


def get_num(n, m):
    my_string = "1" * n
    my_list = list(my_string)
    left_people = n
    i = 0
    count = 1

    while left_people > 1:
        if my_list[i] == "1":
            if count == m:
                my_list[i] = "0"
                count = 1
                left_people -= 1
            else:
                count += 1
        i = (i + 1) % n

    return my_list.index("1") + 1

