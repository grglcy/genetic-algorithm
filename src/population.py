from individual import Individual
from random import Random

rand = Random()


class Population(object):

    def __init__(self, size):
        self.members = list()
        for current in range(0, size):
            self.members.append(Individual())

    def __str__(self):
        return_string = ""
        position = 0
        for member in self.members:
            return_string += "%d:\tx: %e\ty: %e\tfit: %e\n" %\
                             (position, member.x, member.y, member.fitness())
            position += 1
        return_string += "Average fit:\t%e" % self.avg_fitness()
        return return_string

    def fitness_function(self):
        for member in self.members:
            member.fitness()

    def total_fitness(self):
        total = 0
        for member in self.members:
            total += member.fitness()
        return total

    def avg_fitness(self):
        return float(self.total_fitness() / len(self.members))

    def roulette(self, divisor=1):
        total = self.total_fitness() / divisor
        position = rand.uniform(0, total)

        for member in self.members:
            position -= member.fitness() / divisor
            if position <= 0:
                return member

    def advance_generation(self):
        self.fitness_function()
        parents = list()
        for i in range(0, len(self.members)):
            parents.append(self.roulette())

        children = list()
        for i in range(0, len(parents) - 1, 2):
            one, two = self.members[i].crossover(parents[i + 1])
            children.append(one)
            children.append(two)
        self.members = children
