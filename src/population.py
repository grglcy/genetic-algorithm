from individual import Individual
from random import Random

rand = Random()


class Population(object):

    def __init__(self, size):
        self.members = []
        for current in range(0, size):
            self.members.append(Individual())

    def fitness_function(self):
        for member in self.members:
            member.fitness_function()

    def total_fitness(self):
        total = 0
        for member in self.members:
            total += member.fitness
        return total

    def roulette(self, divisor=1):
        total = self.total_fitness() / divisor
        position = rand.uniform(0, total)
        for member in self.members:
            position -= member.fitness / divisor
            if position <= 0:
                return member

    def advance_generation(self):
        crossover_members = []
        crossover_members.append(self.roulette())
