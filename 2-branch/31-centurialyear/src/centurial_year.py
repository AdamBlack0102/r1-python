"""write your code in method"""


def get_year(year):
    if year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False
