def process_steps(steps):
    line_coords = set()
    x = 0
    y = 0
    for step in steps.split(','):
        direction = step[0]
        distance = int(step[1:])
        for _ in range(distance):
            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1
            line_coords.add((x, y))
    return line_coords


def man_dist(coord):
    return abs(coord[0]) + abs(coord[1])


with open('input.txt') as f:
    inputs = f.readlines()

line1_coords = process_steps(inputs[0])
line2_coords = process_steps(inputs[1])
intersections = line1_coords.intersection(line2_coords)

closest_dist = sorted([man_dist(intersection) for intersection in intersections])[0]
print(f'Manhattan distance for closest point is: {closest_dist}')
