from intcode import Intcode

def print_map():
    for y in range(26, -25, -1):
        row = ''
        for x in range(-25, 26):
            tile = tile_map.get((x, y))
            if (x, y) == loc:
                row += 'D'
            elif tile is None:
                row += ' '
            elif tile == 2:
                row += 'O'
            elif tile == 0:
                row += '█'
            elif tile == 1:
                row += '░'
        print(row)
    print(' ')


with open('repair.ic') as f:
    inputs = f.read()

memory = [int(value) for value in inputs.split(',')]


ic = Intcode(memory, inputs=[1, 2, 4, 3, 1, 2, 3, 1, 2, 3, 1, 2])
#ic = Intcode(memory)
ic.io = False

tile_map = {(0, 0): 1}
last_loc = (0, 0)
loc = (0, 0)

stop = False
while True:
    if len(ic.inputs) < 1:
        direction = input('1-N, 2-S, 3-W, 4-E')
        while direction not in ['1', '2', '3', '4']:
            direction = input('1-N, 2-S, 3-W, 4-E')
        direction = int(direction)
        ic.inputs.append(direction)
        if direction == 1:
            loc = (loc[0], loc[1]+1)
        elif direction == 2:
            loc = (loc[0], loc[1]-1)
        elif direction == 3:
            loc = (loc[0]-1, loc[1])
        elif direction == 4:
            loc = (loc[0]+1, loc[1])
    else:
        direction = ic.inputs[0]
        if direction == 1:
            loc = (loc[0], loc[1]+1)
        elif direction == 2:
            loc = (loc[0], loc[1]-1)
        elif direction == 3:
            loc = (loc[0]-1, loc[1])
        elif direction == 4:
            loc = (loc[0]+1, loc[1])

    while len(ic.outputs) < 1:
        if ic.step():
            stop = True
            break
    if stop:
        break
    status_code = ic.outputs.pop()
    print(loc, status_code)
    tile_map[loc] = status_code

    if status_code == 0:
        loc = last_loc
    else:
        last_loc = loc
    print_map()
