from math import atan2
from sys import argv


def angle_calc(a_point, b_point):
    ax, ay = a_point
    bx, by = b_point
    return atan2(by-ay, bx-ax)


with open(argv[1]) as f:
    inputs = f.read()

asteroid_map = {}

for y, row in enumerate(inputs.splitlines()):
    for x, asteroid in enumerate(row):
        if asteroid != '.':
            asteroid_map[(x, y)] = 0

for asteroid in asteroid_map.keys():
    angle_list = []
    for other_asteroid in asteroid_map.keys():
        if other_asteroid == asteroid:
            continue
        angle_list.append(angle_calc(asteroid, other_asteroid))
    asteroid_map[asteroid] = len(list(set(angle_list)))  # Remove blocked asteroids

best_asteroid = sorted(asteroid_map, key=asteroid_map.get)[-1]

print(f'Best asteroid location: {best_asteroid}')
print(f'Able to see {asteroid_map[best_asteroid]} asteroids')
