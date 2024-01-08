# -*- coding: utf-8 -*-

def count_stairs(n: int, memo) -> int:
    if n < 0:
        return 0

    if n in memo:
        return memo[n]

    step_1 = count_stairs(n - 1, memo)
    step_2 = count_stairs(n - 2, memo)
    step_3 = count_stairs(n - 3, memo)
    memo[n] = step_3 + step_2 + step_1
    return memo[n]


def climbing_stairs2(n: int) -> int:
    return count_stairs(n, {0: 1})
