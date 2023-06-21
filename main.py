import numpy

a = 50
b = 100


def add_2_nums(a, b):
    return a + b


def add_4_nums(a, b, c, d):
    return add_2_nums(a, b) + add_2_nums(c, d)


print(add_2_nums(a, b))
