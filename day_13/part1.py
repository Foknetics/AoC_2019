from intcode import Intcode

with open('paddle.ic') as f:
    inputs = f.read()

memory = [int(value) for value in inputs.split(',')]

ic = Intcode(memory)
ic.io = False

game_map = {}

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
    game_map[(x, y)] = tile_id


blocks = 0
for coord in game_map.keys():
    if game_map[coord] == 2:
        blocks += 1

print(f'Initial game loads with {blocks} block tiles')
