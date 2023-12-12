# -*- coding: utf-8 -*--

from typing import (
    List
)


def _33_search_in_rotated_sorted_array(a: List[int], target: int) -> int:
    if a is None or len(a) == 0:
        return -1

    left, right, end = 0, len(a) - 1, len(a) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if a[mid] == target:
            return mid
        elif a[0] <= a[mid]:
            if (a[0] <= target) and (a[mid] > target):
                right = mid
            else:
                left = mid
        elif a[mid] <= a[end]:
            if (a[mid] < target) and (a[end] >= target):
                left = mid
            else:
                right = mid

    if a[left] == target:
        return left

    if a[right] == target:
        return right

    return -1
