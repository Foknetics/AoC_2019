import time

from intcode import Intcode

with open('paddle.ic') as f:
    inputs = f.read()

memory = [int(value) for value in inputs.split(',')]

ic = Intcode(memory)
ic.memory[0] = 2
ic.io = False

game_map = {}
ball_loc = (0, 0)
paddle_loc = (0, 0)
score = 0

stop = False
while True:
    while len(ic.outputs) < 3:
        if ic.step():
            stop = True
            break
    if stop:
        break

    x, y, tile_id = ic.outputs
    ic.outputs = []

    if x == -1 and y == 0:
        score = tile_id
    else:
        game_map[(x, y)] = tile_id
        if tile_id == 3:
            paddle_loc = (x, y)
        elif tile_id == 4:
            ball_loc = (x, y)

    if ic.inputs == []:
        output = ''
        for y in range(23):
            row = ''
            for x in range(45):
                if (x, y) == paddle_loc:
                    row += '▀'
                else:
                    tile_id = game_map.get((x, y), 0)
                    if tile_id == 0:
                        row += ' '
                    elif tile_id == 1:
                        row += '█'
                    elif tile_id == 2:
                        row += '░'
                    elif tile_id == 4:
                        row += '.'
            output += row+'\n'
        output += f'Score: {score}'
        print(output, end='\r')
        time.sleep(.05)

    if ball_loc[0] > paddle_loc[0]:
        ic.inputs = [1]
    elif ball_loc[0] < paddle_loc[0]:
        ic.inputs = [-1]
    else:
        ic.inputs = [0]
