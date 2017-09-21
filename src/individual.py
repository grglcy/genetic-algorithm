from math import pow, sin, pi


class Individual(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def fitness_function(self):
        x = self.x
        y = self.y
        n = 9
        return pow(15*x*y*(1-x)*(1-y)*sin(n*pi*x)*sin(n*pi*y), 2)
