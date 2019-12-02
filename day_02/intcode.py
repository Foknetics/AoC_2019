def process(memory):
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
            return memory[0]
        else:
            raise ValueError(f'Invalid opcode: {opcode} '
                             f'at address: {instruction_pointer}')
