import math

with open('input.txt') as f:
    modules = f.readlines()

def fuel_needed(mass):
    mass = int(mass)/3  # Parse the module mass and divide by 3
    mass = math.floor(mass)  # Round Down
    return mass - 2  # Subtract 2

def real_fuel_needed(mass):
    total_fuel = 0
    new_fuel = fuel_needed(mass)
    while new_fuel > 0:  # Continue to add fuel for previously added mass
        total_fuel += new_fuel
        new_fuel = fuel_needed(new_fuel)
    return total_fuel

total_fuel = sum([real_fuel_needed(mass) for mass in modules])

print('Total fuel required: {}'.format(total_fuel))
