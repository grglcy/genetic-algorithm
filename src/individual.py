from math import pow, sin, pi
from random import Random


class Individual(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rand = Random()

    def fitness_function(self):
        x = self.x
        y = self.y
        n = 9
        return pow(15*x*y*(1-x)*(1-y)*sin(n*pi*x)*sin(n*pi*y), 2)

    def crossover(self, spouse):
        temp = self.x
        self.x = spouse.x
        spouse.x = temp

    def mutate(self):
        if self.rand.randint(1, 10) % 2 == 0:
            self.x = self.rand.random()
        else:
            self.y = self.rand.random()
