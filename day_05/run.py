from intcode import process

with open('input.txt') as f:
    inputs = f.read()

memory = [int(value) for value in inputs.split(',')]
process(memory)
