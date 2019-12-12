from copy import deepcopy
from itertools import combinations

with open('input.txt') as f:
    inputs = f.read()

axes = ['x', 'y', 'z']
moons = []
match_data = []

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

    match_moon = {}
    match_moon['position'] = {
        'x': [],
        'y': [],
        'z': []
    }
    match_moon['velocity'] = {
        'x': [],
        'y': [],
        'z': []
    }
    match_data.append(match_moon)

og_moons = deepcopy(moons)

steps = 100000
for _ in range(steps):
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

    #print(f'Step {_+1}')
    for index, moon in enumerate(moons):
        for value in ['position', 'velocity']:
            for axis in axes:
                if og_moons[index][value][axis] == moons[index][value][axis]:
                    match_data[index][value][axis].append(_)
