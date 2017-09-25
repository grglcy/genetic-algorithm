import argparse
from population import Population

args = argparse.ArgumentParser()
args.add_argument("pop", help="Population size", type=int)
args = args.parse_args()

pop = Population(args.pop)

while True:
    print(pop)
    input("Advance...")
    pop.advance_generation()
