# -*- coding: utf-8 -*-

from typing import (
    List,
)


def two_sum7(nums: List[int], target: int) -> List[int]:
    # write your code here
    if nums is None or len(nums) == 0:
        return []

    nums.sort()
    left, right, t = 0, 0, abs(target)
    while right < len(nums):
        if left == right:
            right += 1
            continue
        cur_diff = nums[right] - nums[left]
        if cur_diff == t:
            return [nums[left], nums[right]]
        elif cur_diff > t:
            left += 1
        else:
            right += 1

    return [-1, -1]
