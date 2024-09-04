"""write your code in method"""


def get_year():
    year = int(input())
    while True:
        year += 1
        str_year = str(year)
        if len(set(str_year)) == len(str_year):
            print(year)
            return






