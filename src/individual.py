from math import pow, sin, pi


def fitness_function(x, y):
    n = 9
    return pow(15*x*y*(1-x)*(1-y)*sin(n*pi*x)*sin(n*pi*y), 2)