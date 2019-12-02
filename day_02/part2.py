from itertools import product

from intcode import process

with open('input.txt') as f:
    inputs = f.read()

initial_memory = [int(value) for value in inputs.split(',')]

for noun, verb in product(range(100), repeat=2):
    memory = initial_memory.copy()
    memory[1] = noun
    memory[2] = verb
    if process(memory) == 19690720:
        print(f'100 * {noun} + {verb} = {100*noun+verb}')
        break
