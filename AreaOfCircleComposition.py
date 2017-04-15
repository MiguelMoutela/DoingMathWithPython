from math import cos, pi
from keyword import *

'''
def distance(x1, y1, x2, y2):
    dx = x2-x1
    print(dx)
    dy = y2-y1
    print(dy)
    dsquared = dx**2 + dy**2
    print(dsquared)
    result = dsquared**0.5
    return result

def area_of_circle(radius):
    result = 3.14 * radius**2
    return result

def area_circle_two_points(xc, yc, xp, yp):
    area = area_of_circle(distance(xc, yc, xp, yp))
    print(area)

area_circle_two_points(0, 0, 3, 4)
'''

def is_divisible_by_2_or_5(n):
    """
    >>> is_divisible_by_2_or_5(8)
    True
    >>> is_divisible_by_2_or_5(7)
    False
    >>> is_divisible_by_2_or_5(5)
    True
    >>> is_divisible_by_2_or_5(9)
    False
    """
    return n % 2 == 0 or n % 5 == 0

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

    print(is_divisible_by_2_or_5(10))
    













