# -*- coding: utf-8 -*-

from typing import (
    List,
)
import collections


def min_elements(arr: List[int]) -> int:
    # write your code here
    if not arr:
        return 0

    total_sum, min_set, n = sum(arr), float('inf'), len(arr)
    queue = collections.deque()
    queue.append([])
    for num in arr:
        for i in range(len(queue)):
            next_subset = list(queue[i])
            next_subset.append(num)
            sum_next_subset = sum(next_subset)
            if sum_next_subset > total_sum - sum_next_subset:
                min_set = min(min_set, len(next_subset))
            queue.append(next_subset)

    return min_set
