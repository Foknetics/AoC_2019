math_ops = {
    1: '+',
    2: '*'
}


def process(memory):
    instruction_pointer = 0
    while True:
        opcode = memory[instruction_pointer]
        if opcode in math_ops.keys():
            parm1, parm2, parm3 = [memory[instruction_pointer + offset] for offset in range(1, 4)]
            memory[parm3] = eval(f'{memory[parm1]} {math_ops[opcode]} {memory[parm2]}')
            instruction_pointer += 4
        elif opcode == 99:
            return memory[0]
        else:
            raise ValueError(f'Invalid opcode: {opcode} '
                             f'at address: {instruction_pointer}')
