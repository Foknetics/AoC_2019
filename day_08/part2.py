from sys import argv


with open(argv[1]) as f:
    inputs = f.read()[:-1]


layers = []
layer = []
row = []

image = [[None for _ in range(25)] for _ in range(6)]

column = 0
row = 0
for char in inputs:
    digit = int(char)
    if digit < 2 and image[row][column] is None:
        if digit == 1:
            image[row][column] = '█'
        else:
            image[row][column] = ' '
    column += 1
    if column >= 25:
        column = 0
        row += 1
        if row >= 6:
            row = 0


for row in image:
    print(''.join(row))
