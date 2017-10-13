import os
from multiprocessing import Process, Queue
from lifecycle import Lifecycle
from file import File
from time import sleep
import time

param_example = {'population_size': 10,
                 'elite': round(0.1 * 10),
                 'crossover': round(0.6 * 10),
                 'epochs': 1000,
                 'iter': 0}


def gen_param(pop, elite, crossover, epochs):
    return {'population_size': pop,
            'elite': round(elite * pop),
            'crossover': round(crossover * pop),
            'epochs': epochs}


outputs = Queue()


def run_instance(instance, output_list):
    instance.start()
    output_list.put(instance.get_csv())
    print(instance.id)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


output_file = File("output.csv", ['id', 'best_fit'] + list(param_example))

output_file.write_header()

instances = list()

id = 0

for i in [x * 1 for x in range(0, 100)]:
    instances.append(Process(name="Thread-%d" % i, target=run_instance,
                             args=[Lifecycle(id, gen_param(50, 0, 0.5, 500)), outputs]))
    id += 1

start_time = time.time()

for instance in instances:
    instance.start()

while len([t for t in instances if t.is_alive()]) != 0:
    print("Processes left: %d" % len([t for t in instances if t.is_alive()]))
    sleep(1)

end_time = time.time()

while not outputs.empty():
    output_file.write_row(outputs.get())

output_file.close()

print("Execution took %f seconds" % (end_time - start_time))
