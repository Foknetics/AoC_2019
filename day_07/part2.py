from sys import argv
from itertools import permutations

from intcode import Intcode


def test_acs(permutation):
    # Prep amplifiers
    amp_a = Intcode(memory.copy(), inputs=[permutation[0]])
    amp_b = Intcode(memory.copy(), inputs=[permutation[1]])
    amp_c = Intcode(memory.copy(), inputs=[permutation[2]])
    amp_d = Intcode(memory.copy(), inputs=[permutation[3]])
    amp_e = Intcode(memory.copy(), inputs=[permutation[4]])

    # Load phase setting
    amp_a.step()
    amp_b.step()
    amp_c.step()
    amp_d.step()
    amp_e.step()

    # Load initial input via mock amp_e output
    amp_e.outputs.append(0)

    while True:
        max_output = amp_e.outputs.pop()
        amp_a.inputs.append(max_output)
        while amp_a.outputs == []:
            if amp_a.step():
                return max_output

        # Load input from amp_a output
        amp_b.inputs.append(amp_a.outputs.pop())
        while amp_b.outputs == []:
            if amp_b.step():
                break

        # Load input from amp_b output
        amp_c.inputs.append(amp_b.outputs.pop())
        while amp_c.outputs == []:
            if amp_c.step():
                break

        # Load input from amp_c output
        amp_d.inputs.append(amp_c.outputs.pop())
        while amp_d.outputs == []:
            if amp_d.step():
                break

        # Load input from amp_d output
        amp_e.inputs.append(amp_d.outputs.pop())
        while amp_e.outputs == []:
            if amp_e.step():
                break


with open(argv[1]) as f:
    inputs = f.read()

memory = [int(value) for value in inputs.split(',')]

thruster_signals = {}

# Phase setting 5 to 9, used exactly once through AMP A-E
for permutation in permutations([5, 6, 7, 8, 9]):
    thruster_signals[test_acs(permutation)] = permutation

highest_signal = sorted(thruster_signals.keys())[-1]

print(f'Highest signal that can be sent to the thrusters is {highest_signal}')
