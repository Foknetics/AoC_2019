from sys import argv
from itertools import permutations

from intcode import Intcode

with open(argv[1]) as f:
    inputs = f.read()

memory = [int(value) for value in inputs.split(',')]

robot_ic = Intcode(memory, inputs=[1])
headings = [0, 90, 180, 270]
heading_index = 0

location = (0, 0)

paint_grid = {}
paint_count = {}

stop = False
while True:
    while len(robot_ic.outputs) < 2:
        if robot_ic.step():
            stop = True
            break
    if stop:
        break

    turn_indicator = robot_ic.outputs.pop()
    paint_color = robot_ic.outputs.pop()

    paint_grid[location] = paint_color
    paint_count[location] = paint_count.get(location, 0) + 1

    if turn_indicator == 0:
        heading_index -= 1
    else:
        heading_index += 1

    heading = headings[heading_index%4]

    if heading == 0:
        location = (location[0], location[1]+1)
    elif heading == 90:
        location = (location[0]+1, location[1])
    elif heading == 180:
        location = (location[0], location[1]-1)
    else:
        location = (location[0]-1, location[1])

    robot_ic.inputs.append(paint_grid.get(location, 0))

for y in range(0, 6):
    row = ''
    for x in range(0, 50):
        if paint_grid.get((x, -y), 0):
            row += '█'
        else:
            row += ' '
    print(row)
