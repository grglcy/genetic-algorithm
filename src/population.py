from individual import Individual


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

    def roulette(self):
        total = self.total_fitness()
        for member in self.members:
            total -= member.fitness
            if total <= 0:
                pass
                # todo: add to crossover list
