import math

with open('input.txt') as f:
    modules = f.readlines()

def fuel_needed(mass):
    mass = int(mass)/3  # Parse the module mass and divide by 3
    mass = math.floor(mass)  # Round Down
    return mass - 2  # Subtract 2

total_fuel = sum([fuel_needed(mass) for mass in modules])

print('Total fuel required: {}'.format(total_fuel))
