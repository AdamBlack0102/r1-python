import math


def pizza_calculation():
    people = int(input('How many people?'))
    pizza = int(input('How many pizzas do you have?'))
    piece = int(input('How many pieces does each pizza have?'))

    total = pizza * piece
    left = total % people
    each_pizza = total // people

    print('Each people gets %d pieces of pizza' % each_pizza)
    print('%d leftover pieces' % left)
