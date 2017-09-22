from individual import Individual


class Population(object):

    def __init__(self, size):
        self.members = []
        for current in range(0, size):
            self.members.append(Individual())

    def fitness_function(self):
        total = 0
        for member in self.members:
            total += member.fitness_function()
        return total

