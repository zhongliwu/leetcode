# -*- coding: utf-8 -*-
from typing import (
    List,
)


def three_sum_closest(numbers: List[int], target: int) -> int:
    # write your code here
    if not numbers:
        return 0

    numbers.sort()
    nearest, total = float('inf'), 0
    for i in range(0, len(numbers) - 2):
        cur_sum = target - numbers[i]
        left, right = i + 1, len(numbers) - 1
        while left < right:
            cur_diff = numbers[left] + numbers[right]
            if nearest > abs(cur_sum - cur_diff):
                nearest = abs(cur_sum - cur_diff)
                total = cur_diff + numbers[i]

            if cur_diff == cur_sum:
                return target
            elif cur_diff > cur_sum:
                right -= 1
            else:
                left += 1

    return total
