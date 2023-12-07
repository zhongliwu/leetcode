# -*- coding: utf-8 -*--

from typing import (
    List
)


class BinarySearch:

    def __init__(self):
        pass

    def q658_find_k_closest_elements(self, a: List[int], target: int, k: int) -> List[int]:
        # write your code here
        if a is None or len(a) == 0:
            return []

        start, end = 0, len(a) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if a[mid] == target:
                start = mid
                end = mid + 1
                break
            elif a[mid] > target:
                end = mid
            else:
                start = mid

        rlt = []
        for i in range(0, k):
            if start < 0:
                rlt.append(a[end])
                end += 1
            elif end >= len(a):
                rlt.append(a[start])
                start -= 1
            elif abs(a[start] - target) > abs(a[end] - target):
                rlt.append(a[end])
                end += 1
            elif abs(a[start] - target) <= abs(a[end] - target):
                rlt.append(a[start])
                start -= 1

        return rlt

    def q33_search_in_rotated_sorted_array(self, a: List[int], target: int) -> int:
        # write your code here
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
