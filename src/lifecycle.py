from population import Population
import matplotlib.pyplot as plt


class Lifecycle(object):
    def __init__(self, id, params):
        self.id = id
        self.params = params
        self.population = Population(self.params["population_size"])
        self.best_fit = list()
        self.average_fit = list()

    def start(self):
        for epoch in range(0, self.params["iter"]):
            elite = round(self.params["elite"] * self.params["population_size"])
            crossover = round((self.params["crossover"]
                               * self.params["population_size"]) / 2)
            self.population.advance_generation(elite, crossover)
            self.best_fit.append(self.population.best_fitness())
            self.average_fit.append(self.population.avg_fitness())

    def best_member(self):
        return self.population.best_member()

    def generate_graph(self, show=False, location=None):
        plt.plot(self.best_fit)
        plt.xlabel("Epoch")
        plt.ylabel("Best fitness")
        if show:
            plt.show()
        if location is not None:
            plt.savefig(location)