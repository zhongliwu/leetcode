# -*- coding: utf-8 -*-

from typing import (
    List,
)


def length_of_lis(nums: List[int]) -> int:
    if nums is None or len(nums) == 0:
        return 0

    dp = [1] * len(nums)
    for i in range(0, len(dp)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[j] + 1, dp[i])

    return max(dp)
