with open('input.txt') as f:
    inputs = f.readlines()

line1 = inputs[0]
line2 = inputs[1]

line1_path = {}
line2_path = {}

x = 0
y = 0
steps = 0
for instruction in line1.split(','):
    direction = instruction[0]
    distance = int(instruction[1:])
    for _ in range(distance):
        steps += 1
        if direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1
        elif direction == 'U':
            y += 1
        elif direction == 'D':
            y -= 1
        if (x, y) not in line1_path:
            line1_path[(x, y)] = steps

x = 0
y = 0
steps = 0
for instruction in line2.split(','):
    direction = instruction[0]
    distance = int(instruction[1:])
    for _ in range(distance):
        steps += 1
        if direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1
        elif direction == 'U':
            y += 1
        elif direction == 'D':
            y -= 1
        if (x, y) not in line2_path:
            line2_path[(x, y)] = steps

line1_coords = set(line1_path.keys())
line2_coords = set(line2_path.keys())

intersections = line1_coords.intersection(line2_coords)

def signal_delay(coord):
    return line1_path[coord] + line2_path[coord]

for intersection in intersections:
    print(f'{intersection}: {signal_delay(intersection)}')
