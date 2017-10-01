from math import pow, sin, pi
from random import Random
from enum import Enum

rand = Random()


class Flag(Enum):
    UNSET = 1,
    PARENT = 2,
    ELITE = 3,
    PERSIST = 4


class Individual(object):

    def __init__(self):
        self.x = self.get_rand_param()
        self.y = self.get_rand_param()
        self.flag = Flag(Flag.UNSET)

    @classmethod
    def from_params(cls, x, y):
        new_individual = Individual()
        new_individual.x = x
        new_individual.y = y
        return new_individual

    def __str__(self):
        return "x: %f\ty: %f\tfit: %f\n" %\
               (self.x, self.y, self.fitness())

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
        rand.randint(1, 10)
        if rand.randint(1, 10) % 2 == 0:
            self.x = self.get_rand_param()
        else:
            self.y = self.get_rand_param()

    @staticmethod
    def get_rand_param():
        return rand.uniform(0, 1)

    def set_flag(self, flag):
        if self.flag is Flag.UNSET:
            self.flag = flag
            return True
        else:
            return False

    def reset_flag(self):
        self.flag = Flag.UNSET
