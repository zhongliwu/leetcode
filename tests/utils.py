# -*- coding: utf-8 -*--


def compare_arr(array_a: list[int], array_b: list[int]) -> bool:
    if len(array_a) != len(array_b):
        return False

    for i in range(0, len(array_a)):
        if array_a[i] != array_b[i]:
            return False

    return True
