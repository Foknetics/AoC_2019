from sys import argv

from intcode import Intcode

with open(argv[1]) as f:
    inputs = f.read()


memory = [int(value) for value in inputs.split(',')]
ic = Intcode(memory)
