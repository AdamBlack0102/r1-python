"""write your code in method"""


def calculate():
    num = int(input(''))
    soilders_list = []
    for i in range(0, num):
        soilders_list.append(int(input('')))

    min_times = 0
    max_height = max(soilders_list)
    max_times = soilders_list.index(max_height)
    min_height = min(soilders_list)

    soilders_list.remove(max_height)
    soilders_list = [max_height] + soilders_list

    while soilders_list[num-1-min_times] != min_height:
        min_times += 1
    print(max_times + min_times)
    pass



