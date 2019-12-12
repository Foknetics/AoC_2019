from itertools import combinations

with open('input.txt') as f:
    inputs = f.read()

axes = ['x', 'y', 'z']
moons = []

for moon_scan in inputs.splitlines():
    moon = {}
    x, y, z = [int(coord[2:]) for coord in moon_scan[1:-1].split(', ')]
    moon['position'] = {
        'x': x,
        'y': y,
        'z': z
    }
    moon['velocity'] = {
        'x': 0,
        'y': 0,
        'z': 0
    }
    moons.append(moon)

for step in range(1000):
    # Apply gravity to update velocity
    for moon_a, moon_b in combinations(moons, r=2):
        for axis in axes:
            if moon_a['position'][axis] < moon_b['position'][axis]:
                moon_a['velocity'][axis] += 1
                moon_b['velocity'][axis] -= 1
            elif moon_a['position'][axis] > moon_b['position'][axis]:
                moon_a['velocity'][axis] -= 1
                moon_b['velocity'][axis] += 1

    # Apply velocity
    for moon in moons:
        for axis in axes:
            moon['position'][axis] += moon['velocity'][axis]

total_energy = 0
for moon in moons:
    potential_energy = sum([abs(moon['position'][axis]) for axis in axes])
    kinetic_energy = sum([abs(moon['velocity'][axis]) for axis in axes])
    total_energy += potential_energy*kinetic_energy

print(f'After 1000 steps the total energy in the system is {total_energy}')
