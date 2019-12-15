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


io_ops = [3, 4]

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


def len_op(operation):
    return {
        1: 3,
        2: 3,
        3: 1,
        4: 1,
        5: 2,
        6: 2,
        7: 3,
        8: 3,
        9: 2,
        99: 0
    }[operation]
