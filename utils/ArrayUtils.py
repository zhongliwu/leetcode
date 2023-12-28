# -*- coding: utf-8 -*--
import copy
from typing import (
    List,
)


def compare_arr(array_a: list[int], array_b: list[int]) -> bool:
    if len(array_a) != len(array_b):
        return False

    array_a.sort()
    array_b.sort()
    for i in range(0, len(array_a)):
        if array_a[i] != array_b[i]:
            return False

    return True


# compare compound lists/matrix
def compare_compound_lists(list_a: List[List[int]], list_b: List[List[int]]):
    if len(list_a) != len(list_b):
        return False

    list_a_copy = copy.deepcopy(list_a)
    list_b_copy = copy.deepcopy(list_b)

    list_a_copy.sort()
    list_b_copy.sort()
    for i in range(len(list_a_copy)):
        if not compare_arr(list_a_copy[i], list_b_copy[i]):
            return False
    return True

