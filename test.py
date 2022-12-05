import argparse
from ast import parse
from art import tprint


parser = argparse.ArgumentParser()

anything = parser.add_argument("--anything", required=True, nargs="+")

args = parser.parse_args()

anything = args.anything

print("\n")
for string in anything:
    tprint(f" {string}")
print("\n")


