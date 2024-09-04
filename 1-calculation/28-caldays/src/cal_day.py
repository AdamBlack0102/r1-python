"""write your code in method"""


def get_day(month, day):

    if month == 3:
        days = day - 4
    elif month == 4:
        days = 27 + day
    elif month == 5:
        days = 57 + day
    elif month == 6:
        days = 88 + day
    elif month == 7:
        days = 118 + day
    elif month == 8:
        days = 149 + day
    elif month == 9:
        days = 180 + day
    elif month == 10:
        days = 210 + day
    elif month == 11:
        days = 241 + day
    else:
        days = 271 + day

    return days

