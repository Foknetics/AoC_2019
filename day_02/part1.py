with open('input.txt') as f:
    program = f.read()

program = [int(instruction) for instruction in program.split(',')]
program[1] = 12
program[2] = 2

for index in range(len(program))[::4]:
    opcode = program[index]
    if opcode == 1 or opcode == 2:
        first_reg = program[index+1]
        second_reg = program[index+2]
        third_reg = program[index+3]
        if opcode == 1:
            program[third_reg] = program[first_reg] + program[second_reg]
        else:
            program[third_reg] = program[first_reg] * program[second_reg]
    elif opcode == 99:
        break

print(f'Final value in register 0: {program[0]}')
