import os
import argparse
from population import Population
from time import sleep
import matplotlib.pyplot as plt


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


best_fit = list()

args = argparse.ArgumentParser()
args.add_argument("pop", help="Population size", type=int)
args.add_argument("iter", help="Iterations", type=int)
args.add_argument("-w", "--wait", help="Time in seconds to wait between iterations", type=int, default=0)
args = args.parse_args()

pop = Population(args.pop)

for i in range(0, args.iter):
    cls()
    print("Epoch: %d " % i)
    pop.advance_generation()
    best = pop.best_fitness()
    best_fit.append(pop.avg_fitness())
    #input("...")
    sleep(args.wait)

plt.plot(best_fit)
plt.xlabel("Epoch")
plt.ylabel("Fitness")
plt.show()
