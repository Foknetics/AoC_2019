from sys import argv
from itertools import permutations

from intcode import Intcode


def test_acs(permutation):
    ic.reboot()
    a_signal = ic.run(inputs=[permutation[0], 0])[0]

    ic.reboot()
    b_signal = ic.run(inputs=[permutation[1], a_signal])[0]

    ic.reboot()
    c_signal = ic.run(inputs=[permutation[2], b_signal])[0]

    ic.reboot()
    d_signal = ic.run(inputs=[permutation[3], c_signal])[0]

    ic.reboot()
    return ic.run(inputs=[permutation[4], d_signal])[0]



with open(argv[1]) as f:
    inputs = f.read()

memory = [int(value) for value in inputs.split(',')]
ic = Intcode(memory)


thruster_signals = {}

# Phase setting 0 to 4, used exactly once through AMP A-E
for permutation in permutations([4, 3, 2, 1, 0]):
    thruster_signals[test_acs(permutation)] = permutation

highest_signal = sorted(thruster_signals.keys())[-1]

print(f'Highest signal that can be sent to the thrusters is {highest_signal}')

