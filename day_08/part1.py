from sys import argv


with open(argv[1]) as f:
    inputs = f.read()[:-1]


layers = []
layer = []
row = []

for char in inputs:
    digit = int(char)
    row.append(digit)
    if len(row) >= 25:
        layer.append(row)
        row = []
        if len(layer) >= 6:
            layers.append(layer)
            layer = []

zeros_and_layers = {}

for layer in layers:
    digits = []
    for row in layer:
        for digit in row:
            digits.append(digit)
    zeros_and_layers[digits.count(0)] = digits

correct_layer = zeros_and_layers[sorted(zeros_and_layers.keys())[0]]

print(correct_layer.count(1)*correct_layer.count(2))
