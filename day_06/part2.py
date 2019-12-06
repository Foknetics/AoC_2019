from sys import argv


def potential_jumps(obj):
    others = []
    for orbit in orbits:
        if obj in orbits[orbit]:
            others.append(orbit)
    return set(orbits.get(obj, []) + others)


with open(f'{argv[1]}.txt') as f:
    inputs = f.read()

inputs = inputs.splitlines()

orbits = {}

for orbit in inputs:
    obj_1, obj_2 = orbit.split(')')
    if obj_1 in orbits:
        orbits[obj_1].append(obj_2)
    else:
        orbits[obj_1] = [obj_2]

bad_nodes = set()
path = ['YOU']
obj = 'YOU'
while obj != 'SAN':
    jumps = potential_jumps(obj).difference(bad_nodes).difference(set(path))
    if len(jumps) == 0:
        bad_nodes.add(obj)
        path = path[:-1]
    elif len(jumps) == 1:
        path.append(jumps.pop())
        obj = path[-1]
    else:
        path.append(jumps.pop())
        obj = path[-1]

print(f'Least possible transfers to get into orbit with Santa: {len(path)-3}')
