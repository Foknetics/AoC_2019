from operator import (
    add,
    multiply
)


math_ops = {
    1: add,
    2: multiply
}


def process(memory):
    instruction_pointer = 0
    while True:
        opcode = memory[instruction_pointer]
        if opcode in math_ops.keys():
            parm1, parm2, parm3 = [memory[instruction_pointer + offset] for offset in range(1, 4)]
            memory[parm3] = math_ops[opcode](memory[parm1], memory[parm2])
            instruction_pointer += 4
        elif opcode == 99:
            return memory[0]
        else:
            raise ValueError(f'Invalid opcode: {opcode} '
                             f'at address: {instruction_pointer}')
