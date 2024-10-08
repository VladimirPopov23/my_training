# true_math

from math import inf


def divide(first, second):
    if second == 0:
        res_ = inf
    else:
        res_ = first / second
    return res_
