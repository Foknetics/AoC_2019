with open('input.txt') as f:
    inputs = f.read()

initial_program = [int(instruction) for instruction in inputs.split(',')]

for noun in range(0, 100):
    for verb in range(0, 100):
        program = initial_program.copy()
        program[1] = noun
        program[2] = verb

        for index in range(len(program))[::4]:
            opcode = program[index]
            if opcode == 1 or opcode == 2:
                address_1 = program[index+1]
                address_2 = program[index+2]
                address_3 = program[index+3]
                if opcode == 1:
                    program[address_3] = program[address_1] + program[address_2]
                else:
                    program[address_3] = program[address_1] * program[address_2]
            elif opcode == 99:
                if program[0] == 19690720:
                    print(100*noun+verb)
                break
            else:
                continue
