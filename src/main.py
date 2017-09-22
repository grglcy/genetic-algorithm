import argparse
from population import Population

args = argparse.ArgumentParser()
args.add_argument("pop", help="Population size", type=int)
args = args.parse_args()

pop = Population(10)

print("%d" % pop.fitness_function())
