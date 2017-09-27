import argparse
from population import Population

args = argparse.ArgumentParser()
args.add_argument("pop", help="Population size", type=int)
args = args.parse_args()

pop = Population(args.pop)

for i in range(0, 1000):
    pop.advance_generation()
    best = pop.best_fitness()
    print(pop)
