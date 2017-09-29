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
        return_string += "Average fit:\t%e\n" % self.avg_fitness()
        best = self.best_fitness()
        return_string += "Best fit:\tx:%e,\ty:%e\tf:%e" %\
                         (best.x, best.y, best.fitness())
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

    def best_fitness(self):
        best_member = self.members[0]

        for member in self.members:
            if float(member.fitness()) > best_member.fitness():
                best_member = member
        return best_member

    def roulette(self, divisor=1):
        total = self.total_fitness() / divisor
        position = rand.uniform(0, total)

        for member in self.members:
            position -= member.fitness() / divisor
            if position <= 0:
                #print(member)
                return member

    def mutate(self, chance):
        for member in self.members:
            if rand.random() < chance/100:
                member.mutate()

    def advance_generation(self):
        # todo: elitism
        # todo: don't crossover all
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
        self.mutate(2)
