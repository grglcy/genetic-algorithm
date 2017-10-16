from population import Population
import matplotlib.pyplot as plt


class Lifecycle(object):
    def __init__(self, id, params):
        self.id = id
        self.params = params
        self.population = Population(self.params["population_size"])
        self.best_fit = list()
        self.average_fit = list()
        self.iterations = 0

    def start(self):
        for epoch in range(0, self.params["epochs"]):
            self.iterations += 1
            elite = self.params["elite"]
            crossover = self.params["crossover"]
            mutation = self.params["mutation"]
            self.population.advance_generation(elite, crossover_rate=crossover,
                                               n_arena=4, mutation=mutation)
            self.best_fit.append(self.population.best_fitness())
            self.average_fit.append(self.population.avg_fitness())
            if epoch > 50:
                recent_best = self.best_fit[-50:]
                if max(recent_best) - min(recent_best) < 0.02:
                    break

    def best_fitness(self):
        return self.population.best_fitness()

    def generate_graph(self, show=False, location=None):
        plt.plot(self.best_fit)
        plt.xlabel("Epoch")
        plt.ylabel("Best fitness")
        plt.title(self.get_params())
        if show:
            plt.show()
        if location is not None:
            plt.savefig(location)

    def get_params(self):
        return_string = ("mutation: %d " % self.params['mutation'])
        return_string += ("crossover: %d " % self.params['crossover'])
        return_string += ("elite: %d " % self.params['elite'])
        return_string += ("iter: %d" % self.iterations)
        return return_string

    def get_csv(self):
        id = {'id': self.id}
        best_fitness = {'best_fit': self.best_fitness()}
        iter = {'iter': self.iterations}
        return {**id, **best_fitness, **self.params, **iter}
