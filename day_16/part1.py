with open('input.txt') as f:
    inputs = f.read()[:-1]

def pattern(length, multiplier):
    base_pattern = [0, 1, 0, -1]
    base_pattern_index = 0
    output = []
    while len(output) < length + 1:
        for _ in range(multiplier):
            output.append(base_pattern[base_pattern_index])
        base_pattern_index += 1
        base_pattern_index = base_pattern_index%4
    return output[1:length+1]


def fft(input_list, phase):
    #print(f'Input signal: {input_list}')
    input_list = [int(char) for char in input_list]
    output_list = ''
    for output_index in range(len(input_list)):
        #calculation = ''
        cur_pattern = pattern(len(input_list), output_index+1)
        total = 0
        for input_index, digit in enumerate(input_list):
            #calculation += f'{digit}*{cur_pattern[input_index]} + '
            total += digit*cur_pattern[input_index]
        #calculation = calculation[:-2] + f'= {abs(total)%10}'
        #print(calculation)
        output_list += str(abs(total)%10)
    #print(f'After {phase} phase: {output_list}')
    return output_list

for phase in range(1, 101):
    inputs = fft(inputs, phase)

print(f'After 100 phases the first eight digits are: {inputs[:8]}')
