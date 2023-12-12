# -*- coding: utf-8 -*-

from typing import (
    List,
)


def four_sum_count(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    # Write your code here
    sum_of_a_and_b = {}
    for num_a in a:
        for num_b in b:
            cur_sum = num_a + num_b
            sum_of_a_and_b[cur_sum] = sum_of_a_and_b.get(cur_sum, 0) + 1

    sum_count = 0
    for num_c in c:
        for num_d in d:
            cur_sum = (num_c + num_d) * -1
            sum_count += sum_of_a_and_b.get(cur_sum, 0)

    return sum_count


