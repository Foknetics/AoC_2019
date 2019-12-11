from sys import argv
from itertools import permutations

from intcode import Intcode

with open(argv[1]) as f:
    inputs = f.read()

memory = [int(value) for value in inputs.split(',')]

robot_ic = Intcode(memory, inputs=[0])
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

    #print('paint_grid info')
    #for loc in paint_grid.keys():
    #    print(loc, paint_grid[loc])
#
    #print('paint_count info')
    #for loc in paint_count.keys():
    #    print(loc, paint_count[loc])

    print(f'turn indicator: {turn_indicator}')

    if turn_indicator == 0:
        heading_index -= 1
        print('Turn Left')
    else:
        heading_index += 1
        print('Turn Right')

    heading = headings[heading_index%4]

    print(f'Heading: {heading}')

    if heading == 0:
        location = (location[0], location[1]+1)
    elif heading == 90:
        location = (location[0]+1, location[1])
    elif heading == 180:
        location = (location[0], location[1]-1)
    else:
        location = (location[0]-1, location[1])

    print(f'Location: {location}')

    robot_ic.inputs.append(paint_grid.get(location, 0))

print(len(paint_count.keys()))
