from operator import (
    add,
    mul
)


math_ops = {
    1: add,
    2: mul
}


def parse_opcode(opcode):
    opcode = str(opcode).rjust(5, '0')
    instruction = int(opcode[-2:])
    modes = []
    for mode in opcode[:-2]:
        modes.insert(0, int(mode))
    return instruction, modes


def process(memory):
    instruction_pointer = 0
    while True:
        opcode = memory[instruction_pointer]
        instruction, modes = parse_opcode(opcode)
        if instruction in math_ops.keys():
            if modes[0] == 0:
                parm1 = memory[memory[instruction_pointer+1]]
            else:
                parm1 = memory[instruction_pointer+1]
            if modes[1] == 0:
                parm2 = memory[memory[instruction_pointer+2]]
            else:
                parm2 = memory[instruction_pointer+2]

            parm3 = memory[instruction_pointer+3]

            memory[parm3] = math_ops[instruction](parm1, parm2)
            instruction_pointer += 4
        elif instruction == 3:
            parm1 = memory[instruction_pointer+1]
            memory[parm1] = int(input('Input requested: '))
            instruction_pointer += 2
        elif instruction == 4:
            if modes[0] == 0:
                parm1 = memory[memory[instruction_pointer+1]]
            else:
                parm1 = memory[instruction_pointer+1]
            print(f'Output: {parm1}')
            instruction_pointer += 2
        elif instruction == 5:
            if modes[0] == 0:
                parm1 = memory[memory[instruction_pointer+1]]
            else:
                parm1 = memory[instruction_pointer+1]
            if modes[1] == 0:
                parm2 = memory[memory[instruction_pointer+2]]
            else:
                parm2 = memory[instruction_pointer+2]

            if parm1 != 0:
                instruction_pointer = parm2
            else:
                instruction_pointer += 3
        elif instruction == 6:
            if modes[0] == 0:
                parm1 = memory[memory[instruction_pointer+1]]
            else:
                parm1 = memory[instruction_pointer+1]
            if modes[1] == 0:
                parm2 = memory[memory[instruction_pointer+2]]
            else:
                parm2 = memory[instruction_pointer+2]

            if parm1 == 0:
                instruction_pointer = parm2
            else:
                instruction_pointer += 3
        elif instruction == 7:
            if modes[0] == 0:
                parm1 = memory[memory[instruction_pointer+1]]
            else:
                parm1 = memory[instruction_pointer+1]
            if modes[1] == 0:
                parm2 = memory[memory[instruction_pointer+2]]
            else:
                parm2 = memory[instruction_pointer+2]

            parm3 = memory[instruction_pointer+3]

            if parm1 < parm2:
                memory[parm3] = 1
            else:
                memory[parm3] = 0
            instruction_pointer += 4
        elif instruction == 8:
            if modes[0] == 0:
                parm1 = memory[memory[instruction_pointer+1]]
            else:
                parm1 = memory[instruction_pointer+1]
            if modes[1] == 0:
                parm2 = memory[memory[instruction_pointer+2]]
            else:
                parm2 = memory[instruction_pointer+2]

            parm3 = memory[instruction_pointer+3]

            if parm1 == parm2:
                memory[parm3] = 1
            else:
                memory[parm3] = 0
            instruction_pointer += 4
        elif instruction == 99:
            return memory[0]
        else:
            raise Exception(f'Invalid opcode: {opcode} '
                            f'at address: {instruction_pointer}')
