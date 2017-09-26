import argparse
from population import Population

args = argparse.ArgumentParser()
args.add_argument("pop", help="Population size", type=int)
args = args.parse_args()

pop = Population(args.pop)

for i in range(0, 5000):
    pop.advance_generation()
    best = pop.best_fitness()
    print("Best fit:\tx:%e,\ty:%e\tf:%e" % (best.x, best.y, best.fitness()))
    print("Average fit:\t%e\n" % pop.avg_fitness())
