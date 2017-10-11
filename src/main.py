import os
from lifecycle import Lifecycle


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


ga = Lifecycle(1, {'population_size': 10,
                   'elite': 0.1,
                   'crossover': 0.6,
                   'iter': 1000})

ga.start()

ga.generate_graph(show=True)
