import math
# Constants 
# ------------------
PI = math.pi
E = math.e
# ------------------

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def asin(x):
    return math.asin(x)

def acos(x):
    return math.acos(x)

def atan(x):
    return math.atan(x)

def exp(x):
    return math.exp(x)

def gcd(x, y):
    return math.gcd(x, y)

def fabs(x):
    return math.fabs(x)

def ceil(x):
    return math.ceil(x)

def floor(x):
    return math.floor(x)

def degrees(x):
    return math.degrees(x)

def radians(x):
    return math.radians(x)

def column_multiply(x, y):
    x_list = []
    y_list = []
    x_list.append(x)
    y_list.append(y)

    index = 0
    while x_list[index] > 1:
        x_list.append(x_list[index] // 2)
        y_list.append(y_list[index] * 2)
        index += 1

    result = 0
    for a, b in zip(x_list, y_list):
        if a & 1:
            result += b

    return result


def log(*args):
    return math.log(*args)

def is_prime(n):
    if n % 2 == 0:
        return False 
    x = 2
    while x * x <= n:
        if n % x == 0:
            return False
        x += 1
    return True

def next_prime(n):
    if n <= 2:
        return 2

    while not is_prime(n):
        n += 1
    return n

def lcm(x, y):
    return (x * y) / gcd(x, y)

import random as r
def random_pi():
    in_circle = 0
    out_circle = 0
    for _ in range(10000):
        x = r.random()
        y = r.random()
        if r.random() < 0.5:
            x = -x
        if r.random() < 0.5:
            y = -y
        if (x**2 + y**2)**0.5 > 1:
            out_circle += 1
        else:
            in_circle += 1
    ppi = (in_circle / (out_circle + in_circle)) * 4
    print(ppi)
