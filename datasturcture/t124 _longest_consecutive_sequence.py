# -*- coding: utf-8 -*-

from typing import (
    List,
)


def longest_consecutive(num: List[int]) -> int:
    # write your code here
    if not num:
        return 0

    nums_map = {n: True for n in num}
    ans = 0
    for elem in num:
        if elem - 1 not in nums_map:
            hi = elem + 1
            while hi in nums_map:
                hi += 1
            ans = max(ans, hi - elem)

    return ans
