from intcode_operators import (
    equality_ops,
    io_ops,
    jump_ops,
    len_op,
    math_ops
)


class Intcode:
    def __init__(self, starting_memory=None, inputs=None):
        if starting_memory:
            self.memory = starting_memory
        else:
            self.memory = None
        self.initial_memory = self.memory.copy()
        self.instruction_pointer = 0
        self.stack_trace = []

        if inputs:
            self.inputs = inputs
            self.io = False
        else:
            self.inputs = []
            self.io = True
        self.outputs = []  # Synthetic outputs

    def load(self, filename):
        with open(filename) as f:
            instructions = f.read()
        self.__init__([int(instruction) for instruction in instructions.split(',')])

    def reboot(self):
        if not self.initial_memory:
            raise ValueError('No program loaded into memory, use load("<filename>")')
        self.__init__(self.initial_memory)

    def run(self, inputs=None):
        if not self.memory:
            raise ValueError('No program loaded into memory, use load("<filename>")')

        if inputs:
            self.inputs = inputs
            self.io = False

        end = False
        while not end:
            end = self.step()
        return self.outputs

    def step(self):
        if not self.memory:
            raise ValueError('No program loaded into memory, use load("<filename>")')
        operation, modes = self._next_operation()
        self.stack_trace.append(self._log_op(operation, modes))
        if operation in math_ops.keys():
            modes[2] = 1
            parm1, parm2, parm3 = self._n_parms(3, modes)
            self.memory[parm3] = math_ops[operation](parm1, parm2)
            self.instruction_pointer += 4
        elif operation in io_ops:
            if operation == 3:
                modes[0] = 1
            parm1 = self._n_parms(1, modes)
            if operation == 3:
                if self.io:
                    self.memory[parm1] = int(input('Input requested: '))
                else:
                    self.memory[parm1] = self.inputs.pop(0)
            else:
                if self.io:
                    print(f'Output: {parm1}')
                else:
                    self.outputs.append(parm1)
            self.instruction_pointer += 2
        elif operation in jump_ops.keys():
            parm1, parm2 = self._n_parms(2, modes)
            self.instruction_pointer = jump_ops[operation](self.instruction_pointer, parm1, parm2)
        elif operation in equality_ops.keys():
            modes[2] = 1
            parm1, parm2, parm3 = self._n_parms(3, modes)
            self.memory[parm3] = equality_ops[operation](parm1, parm2)
            self.instruction_pointer += 4
        elif operation == 99:
            return True
        else:
            raise Exception(f'Invalid operation: {operation} '
                            f'at address: {self.instruction_pointer}\n'
                            f'Last valid instruction: {self.stack_trace[-1]}')
        return

    def _next_operation(self):
        opcode = str(self.memory[self.instruction_pointer]).rjust(5, '0')
        return int(opcode[-2:]), [int(opcode[2]), int(opcode[1]), int(opcode[0])]

    def _n_parms(self, n, modes):
        parms = []
        for offset in range(1, n+1):
            if modes[offset-1] == 0:
                parms.append(self.memory[self.memory[self.instruction_pointer+offset]])
            else:
                parms.append(self.memory[self.instruction_pointer+offset])
        if len(parms) == 1:
            return parms[0]
        return parms

    def _log_op(self, operation, modes):
        start = self.instruction_pointer
        end = start + len_op(operation) + 1
        instruction = self.memory[start:end]
        return {
            'operation': operation,
            'modes': modes,
            'instruction': instruction
        }
