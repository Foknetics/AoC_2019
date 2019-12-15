import json

with open('tile_map.json') as tile_data:
    string_map = json.load(tile_data)

tile_map = {}
for coord in string_map.keys():
    x, y = coord[1:-1].split(', ')
    tile_map[(int(x), int(y))] = string_map[coord]

def print_map():
    output = ''
    for y in range(21, -20, -1):
        row = ''
        for x in range(-21, 20):
            tile = tile_map.get((x, y))
            if tile is None:
                row += ' '
            elif tile == 2:
                row += 'O'
            elif tile == 3:
                row += 'o'
            elif tile == 0:
                row += '█'
            elif tile == 1:
                row += '░'
        output += row+'\n'
    print(output, end='\r')

def lacking_oxygen():
    tiles = []
    for coord in tile_map:
        tiles.append(tile_map[coord])
    return 1 in tiles


minutes = 0
while lacking_oxygen():
    minutes += 1
    for coord in tile_map:
        if tile_map[coord] == 2:
            x, y = coord
            if tile_map.get((x+1, y)) == 1:
                tile_map[(x+1, y)] = 3
            if tile_map.get((x-1, y)) == 1:
                tile_map[(x-1, y)] = 3
            if tile_map.get((x, y+1)) == 1:
                tile_map[(x, y+1)] = 3
            if tile_map.get((x, y-1)) == 1:
                tile_map[(x, y-1)] = 3
    #print(f'After {minutes} minutes')
    #print_map()
    for coord in tile_map.keys():
        if tile_map[coord] == 3:
            tile_map[coord] = 2

print(f'Oxygen will spread in {minutes} minutes')
