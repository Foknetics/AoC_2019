from math import (
    atan2,
    pi,
    sqrt
)


def angle_calc(a_point, b_point):
    ax, ay = a_point
    bx, by = b_point
    return atan2(by-ay, bx-ax)


def distance_calc(a_point, b_point):
    ax, ay = a_point
    bx, by = b_point
    return sqrt((bx - ax)**2 + (by-ay)**2)


def next_asteroid(laser_angle):
    sorted_angles = sorted(angle_asteroids.keys())
    cur_angle_index = sorted_angles.index(laser_angle)
    try:
        next_angle = sorted_angles[cur_angle_index+1]
    except IndexError:
        next_angle = sorted_angles[0]

    if len(angle_asteroids[next_angle]) == 0:
        return next_asteroid(next_angle)
    else:
        asteroid = angle_asteroids[next_angle].pop(0)
        return asteroid, next_angle


with open('input.txt') as f:
    inputs = f.read()

asteroid_map = {}

for y, row in enumerate(inputs.splitlines()):
    for x, asteroid in enumerate(row):
        if asteroid != '.':
            asteroid_map[(x, y)] = 0

best_asteroid = (17, 23)

angle_map = {}
distance_map = {}
for asteroid in asteroid_map.keys():
    if asteroid == best_asteroid:
        continue
    angle_map[asteroid] = angle_calc(best_asteroid, asteroid)
    distance_map[asteroid] = distance_calc(best_asteroid, asteroid)

angle_asteroids = {}
for asteroid, angle in angle_map.items():
    if angle in angle_asteroids:
        angle_asteroids[angle].append(asteroid)
    else:
        angle_asteroids[angle] = [asteroid]

for angle in angle_asteroids.keys():
    angle_asteroids[angle] = sorted(angle_asteroids[angle], key=distance_map.get)

laser_angle = -pi
for angle in sorted(angle_asteroids.keys()):
    if angle < -1.5707963267948966 and angle > laser_angle:
        laser_angle = angle

destroyed = 0
while destroyed < 200:
    last_asteroid, laser_angle = next_asteroid(laser_angle)
    destroyed += 1

print(f'200th asteroid to be destroyed: {last_asteroid}')
print(f'{last_asteroid[0]}*100+{last_asteroid[1]}')
print(last_asteroid[0]*100+last_asteroid[1])
