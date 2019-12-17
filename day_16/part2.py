with open('input.txt') as f:
    inputs = f.read()[:-1]

offset = int(inputs[:7])
inputs = list(map(int, inputs))*10000

offset_inputs = inputs[offset:]

for phase in range(100):
    total = 0
    for index, digit in enumerate(reversed(offset_inputs)):
        total += digit
        total = total % 10
        offset_inputs[-(index+1)] = total

print(f'After {phase+1} phases of signal*10,000 the message is: {"".join(map(str, offset_inputs[:8]))}')
