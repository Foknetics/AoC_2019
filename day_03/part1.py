with open('input.txt') as f:
    inputs = f.readlines()

line1 = inputs[0]
line2 = inputs[1]

line1_path = []
line2_path = []

x = 0
y = 0
for instruction in line1.split(','):
    direction = instruction[0]
    distance = int(instruction[1:])
    for _ in range(distance):
        if direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1
        elif direction == 'U':
            y += 1
        elif direction == 'D':
            y -= 1
        line1_path.append((x, y))

x = 0
y = 0
for instruction in line2.split(','):
    direction = instruction[0]
    distance = int(instruction[1:])
    for _ in range(distance):
        if direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1
        elif direction == 'U':
            y += 1
        elif direction == 'D':
            y -= 1
        line2_path.append((x, y))

line1_path = set(line1_path)
line2_path = set(line2_path)

intersections = line1_path.intersection(line2_path)

def man_dist(coord):
    return abs(coord[0]) + abs(coord[])

for intersection in intersections:
    print(f'{intersection}: {man_dist(intersection)}')
