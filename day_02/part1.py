with open('input.txt') as f:
    inputs = f.read()

memory = [int(value) for value in inputs.split(',')]
memory[1] = 12
memory[2] = 2

instruction_pointer = 0
while True:
    opcode = memory[instruction_pointer]
    if opcode == 1 or opcode == 2:
        parm1 = memory[instruction_pointer+1]
        parm2 = memory[instruction_pointer+2]
        parm3 = memory[instruction_pointer+3]
        if opcode == 1:
            memory[parm3] = memory[parm1] + memory[parm2]
        else:
            memory[parm3] = memory[parm1] * memory[parm2]
        instruction_pointer += 4
    elif opcode == 99:
        break
    else:
        print(f'Invalid opcode: {opcode} at position: {instruction_pointer}')
        break

print(f'Final value in register 0: {memory[0]}')
