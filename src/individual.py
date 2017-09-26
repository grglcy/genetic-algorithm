from math import pow, sin, pi
from random import Random

rand = Random()


class Individual(object):

    def __init__(self):
        self.x = rand.uniform(-100, 100)
        self.y = rand.uniform(-100, 100)

    @classmethod
    def from_params(cls, x, y):
        new_individual = Individual()
        new_individual.x = x
        new_individual.y = y
        return new_individual

    def __str__(self):
        return "x: %f\ty: %f\tfit: %f\n" %\
               (self.x, self.y, self.fitness)

    def fitness(self):
        x = self.x
        y = self.y
        n = 9
        return pow(15*x*y*(1-x)*(1-y)*sin(n*pi*x)*sin(n*pi*y), 2)

    def crossover(self, spouse):
        one = Individual.from_params(spouse.x, self.y)
        two = Individual.from_params(self.x, spouse.y)
        return one, two

    def mutate(self):
        if rand.randint(1, 10) % 2 == 0:
            self.x = rand.random()
        else:
            self.y = rand.random()
