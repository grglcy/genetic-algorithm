from multiprocessing import Process, Queue
from lifecycle import Lifecycle
from file import File
from time import sleep
import time

param_example = {'population_size': 10,
                 'elite': round(0.1 * 10),
                 'crossover': round(0.6 * 10),
                 'mutation': 0,
                 'epochs': 1000,
                 'iter': 0}


def gen_param(pop, elite, crossover, epochs, mutation=0):
    return {'population_size': pop,
            'elite': round((elite / 100) * pop),
            'crossover': round((crossover / 100) * pop),
            'mutation': mutation,
            'epochs': epochs}


outputs = Queue()


def run_instance(instance, output_list):
    instance.start()
    output_list.put(instance.get_csv())
    instance.generate_graph(location="images/%d.png" % instance.id, show=False)
    print(instance.id)


output_file = File("output.csv", ['id', 'best_fit'] + list(param_example))
output_file.write_header()

instances = list()
instance_id = 0

for i in range(20, 90, 10):
    for j in range(0, 3):
        instances.append(
            Process(name="Thread-%d" % i, target=run_instance,
                    args=[Lifecycle(instance_id,
                                    gen_param(50, j, i, 500, mutation=5)), outputs]))
        instance_id += 1

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
