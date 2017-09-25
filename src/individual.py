from math import pow, sin, pi
from random import Random


class Individual(object):

    def __init__(self):
        self.rand = Random()
        self.x = self.rand.uniform(-100000, 100000)
        self.y = self.rand.uniform(-100000, 100000)
        self.fitness = 0

    def __str__(self):
        return "x: %f\ty: %f\tfit: %f\n" %\
               (self.x, self.y, self.fitness)

    def fitness_function(self):
        x = self.x
        y = self.y
        n = 9
        self.fitness = pow(15*x*y*(1-x)*(1-y)*sin(n*pi*x)*sin(n*pi*y), 2)

    def crossover(self, spouse):
        temp = self.x
        self.x = spouse.x
        spouse.x = temp

    def mutate(self):
        if self.rand.randint(1, 10) % 2 == 0:
            self.x = self.rand.random()
        else:
            self.y = self.rand.random()
