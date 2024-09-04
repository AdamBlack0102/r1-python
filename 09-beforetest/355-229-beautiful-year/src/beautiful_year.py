"""write your code in method"""

def repeated(given_year):
    given_year_str = str(given_year)
    given_year_str = sorted(given_year_str)
    for i in range(0, len(given_year_str)):
        if given_year_str[i] == given_year_str[i+1]:
            return False
    return True
def get_year():
    given_year = int(input())
    given_year += 1

    while not repeated(given_year):
        given_year += 1
    else:
        print("%d\n", given_year)





