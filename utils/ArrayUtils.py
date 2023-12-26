# -*- coding: utf-8 -*--

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


def compare_compound_lists(list_a: List[List[int]], list_b: List[List[int]]):
    if len(list_a) != len(list_b):
        return False
    for i in range(len(list_a)):
        if not compare_arr(list_a[i], list_b[i]):
            return False
    return True

