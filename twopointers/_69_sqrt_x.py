# -*- coding: utf-8 -*-

import math

"""
q69: Newton-Raphson method
"""


def _69_sqrt_x(x: int) -> int:
    x1 = float(x ** ((len(str(x)) + 1) / 2))
    while (x1 * x1) > x:
        x1 = (x1 + x / x1) / 2

    return int(x1)
