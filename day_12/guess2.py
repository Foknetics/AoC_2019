from copy import deepcopy
from math import gcd
from itertools import combinations


def moon_hash(moons, axis):
    hash_ = []
    for moon in moons:
        hash_.append(moon['position'][axis])
        hash_.append(moon['velocity'][axis])
    return hash_


def least_common_multiple(values):
    lcm = values[0]
    for i in values[1:]:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


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

og_moons = deepcopy(moons)

step_repeats = {}
for axis in axes:
    og_hash = moon_hash(og_moons, axis)

    steps = 0
    while True:
        steps += 1
        for moon_a, moon_b in combinations(moons, r=2):
            if moon_a['position'][axis] < moon_b['position'][axis]:
                moon_a['velocity'][axis] += 1
                moon_b['velocity'][axis] -= 1
            elif moon_a['position'][axis] > moon_b['position'][axis]:
                moon_a['velocity'][axis] -= 1
                moon_b['velocity'][axis] += 1

        # Apply velocity
        for moon in moons:
            moon['position'][axis] += moon['velocity'][axis]

        if moon_hash(moons, axis) == og_hash:
            break
    step_repeats[axis] = steps

lcm_steps = least_common_multiple([step_repeats[axis] for axis in axes])
print(f'Positions and Velocities repeat at {lcm_steps}')
