# -*- coding: utf-8 -*-

from typing import (
    List,
)


def kth_largest_element(k: int, nums: List[int]) -> int:
    # write your code here
    if nums is None or len(nums) == 0:
        return 0

    return quick_select(k, nums, 0, len(nums) - 1)


def quick_select(k: int, nums: List[int], start: int, end: int) -> int:
    if start == end:
        return nums[start]

    left, right, pivot = start, end, nums[(start + end) // 2]
    while left <= right:
        while nums[left] > pivot and left <= right:
            left += 1

        while nums[right] < pivot and left <= right:
            right -= 1

        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    if start + k - 1 <= right:
        return quick_select(k, nums, start, right)

    if start + k - 1 >= left:
        return quick_select(k - (left - start), nums, left, end)

    return nums[right + 1]
