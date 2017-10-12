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
            elite = self.params["elite"]
            crossover = self.params["crossover"]
            self.population.advance_generation(elite, crossover)
            self.best_fit.append(self.population.best_fitness())
            self.average_fit.append(self.population.avg_fitness())

    def best_fitness(self):
        return self.population.best_fitness()

    def generate_graph(self, show=False, location=None):
        plt.plot(self.best_fit)
        plt.xlabel("Epoch")
        plt.ylabel("Best fitness")
        if show:
            plt.show()
        if location is not None:
            plt.savefig(location)

    def get_csv(self):
        id = {'id': self.id}
        best_fitness = {'best_fit': self.best_fitness()}
        return {**id, **best_fitness, **self.params}
