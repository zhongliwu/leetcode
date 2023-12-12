# -*- coding: utf-8 -*--


from typing import (
    List
)


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
