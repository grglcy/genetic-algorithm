import argparse
from individual import Individual

args = argparse.ArgumentParser()
args.add_argument("pop", help="Population size", type=int)
args = args.parse_args()

population = []

for current in range(0, args.pop):
    population.append(Individual())

print(len(population))
