from intcode import process

with open('input.txt') as f:
    inputs = f.read()

memory = [int(value) for value in inputs.split(',')]
memory[1] = 12
memory[2] = 2

print(f'Final value in address 0: {process(memory)}')
