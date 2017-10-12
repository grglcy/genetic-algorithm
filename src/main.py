import os
from lifecycle import Lifecycle
from file import File

param_example = {'population_size': 10,
                 'elite': round(0.1 * 10),
                 'crossover': round(0.6 * 10),
                 'iter': 1000}


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


output_file = File("output.csv", ['id', 'best_fit'] + list(param_example))

ga = Lifecycle(1, param_example)

ga.start()

output_file.write_header()

output_file.write_row(ga.get_csv())

output_file.close()

ga.generate_graph(show=True)
