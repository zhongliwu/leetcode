# -*- coding: utf-8 -*-

from typing import (
    List,
)


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    # write your code here
    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        return False

    m, n = len(matrix), len(matrix[0])
    left_i, left_j, right_i, right_j = 0, 0, m - 1, n - 1
    while left_i * n + left_j + 1 < right_i * n + right_j:
        mid_idx = (left_i * n + left_j + right_i * n + right_j) // 2
        mid_i, mid_j = mid_idx // n, mid_idx % n
        mid = matrix[mid_i][mid_j]
        if mid == target:
            return True
        elif mid < target:
            left_i, left_j = mid_i, mid_j
        else:
            right_i, right_j = mid_i, mid_j

    if matrix[left_i][left_j] == target:
        return True

    if matrix[right_i][right_j] == target:
        return True

    return False
