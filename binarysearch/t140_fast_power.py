# -*- coding: utf-8 -*-


def fast_power(a: int, b: int, n: int) -> int:
    # write your code here
    if n == 0:
        return 1 % b

    if n == 1:
        return a % b

    product = fast_power(a, b, n // 2)
    mod = product * product
    if n % 2 == 1:
        mod *= (a % b)

    return mod % b
