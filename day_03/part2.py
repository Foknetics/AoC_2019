def process_steps(instructions):
    line_path = {}
    x = 0
    y = 0
    steps = 0
    for step in instructions.split(','):
        direction = step[0]
        distance = int(step[1:])
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
            if (x, y) not in line_path:
                line_path[(x, y)] = steps
    return line_path


def signal_delay(coord):
    return line1_path[coord] + line2_path[coord]


with open('input.txt') as f:
    inputs = f.readlines()

line1_path = process_steps(inputs[0])
line2_path = process_steps(inputs[1])

line1_coords = set(line1_path.keys())
line2_coords = set(line2_path.keys())
intersections = line1_coords.intersection(line2_coords)

lowest_signal = sorted([signal_delay(intersection) for intersection in intersections])[0]
print(f'Lowest signal delay is: {lowest_signal}')
