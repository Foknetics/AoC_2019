from operator import (
    add,
    mul
)


math_ops = {
    1: add,
    2: mul
}


def jump_if_true(pointer, parm1, parm2):
    if parm1 != 0:
        return parm2
    else:
        return pointer+3


def jump_if_false(pointer, parm1, parm2):
    if parm1 == 0:
        return parm2
    else:
        return pointer+3


jump_ops = {
    5: jump_if_true,
    6: jump_if_false
}


def less_than(parm1, parm2):
    if parm1 < parm2:
        return 1
    return 0


def equal(parm1, parm2):
    if parm1 == parm2:
        return 1
    return 0


equality_ops = {
    7: less_than,
    8: equal
}


def parse_opcode(opcode):
    opcode = str(opcode).rjust(5, '0')
    instruction = int(opcode[-2:])
    modes = []
    for mode in opcode[:-2]:
        modes.insert(0, int(mode))
    return instruction, modes


def n_parms(n, memory, pointer, modes):
    parms = []
    for offset in range(1, n+1):
        if len(parms) == 2:
            parms.append(memory[pointer+offset])
            continue
        if modes[offset-1] == 0:
            parms.append(memory[memory[pointer+offset]])
        else:
            parms.append(memory[pointer+offset])
    if len(parms) == 1:
        return parms[0]
    return parms


def process(memory):
    instruction_pointer = 0
    while True:
        opcode = memory[instruction_pointer]
        instruction, modes = parse_opcode(opcode)
        if instruction in math_ops.keys():
            parm1, parm2, parm3 = n_parms(3, memory, instruction_pointer, modes)
            memory[parm3] = math_ops[instruction](parm1, parm2)
            instruction_pointer += 4
        elif instruction == 3:
            parm1 = memory[instruction_pointer+1]
            memory[parm1] = int(input('Input requested: '))
            instruction_pointer += 2
        elif instruction == 4:
            parm1 = n_parms(1, memory, instruction_pointer, modes)
            print(f'Output: {parm1}')
            instruction_pointer += 2
        elif instruction in jump_ops.keys():
            parm1, parm2 = n_parms(2, memory, instruction_pointer, modes)
            instruction_pointer = jump_ops[instruction](instruction_pointer, parm1, parm2)
        elif instruction in equality_ops.keys():
            parm1, parm2, parm3 = n_parms(3, memory, instruction_pointer, modes)
            memory[parm3] = equality_ops[instruction](parm1, parm2)
            instruction_pointer += 4
        elif instruction == 99:
            return memory[0]
        else:
            raise Exception(f'Invalid opcode: {opcode} '
                            f'at address: {instruction_pointer}')
