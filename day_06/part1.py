from sys import argv

with open(f'{argv[1]}.txt') as f:
    inputs = f.read()

inputs = inputs.splitlines()

orbits = {}
objects = []

for orbit in inputs:
    obj_1, obj_2 = orbit.split(')')
    if obj_1 in orbits:
        orbits[obj_1].append(obj_2)
    else:
        orbits[obj_1] = [obj_2]

    if obj_1 not in objects:
        objects.append(obj_1)
    if obj_2 not in objects:
        objects.append(obj_2)

orbitted = []
for orbit in orbits:
    for obj in orbits[orbit]:
        orbitted.append(obj)

orbit_data = []
for obj in objects:
    direct = 0
    if obj in orbitted:
        direct = 1
    else:
        orbit_data.append((obj, 0, 0))
        continue

    indirect = 0
    traversed = []
    for orbit in orbits:
        if obj in orbits[orbit]:
            next_obj = orbit
            traversed.append(next_obj)

    while next_obj in orbitted:
        indirect += 1
        for orbit in orbits:
            if next_obj in orbits[orbit] and orbit not in traversed:
                next_obj = orbit
                traversed.append(next_obj)
                break
    orbit_data.append((obj, 1, indirect))

total = 0
for data in orbit_data:
    total += data[1] + data[2]

print(f'total direct and indirect: {total}')
