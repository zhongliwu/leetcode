# -*- coding: utf-8 -*-

from typing import (
    List,
)


def check_col(image: List[List[str]], col: int) -> bool:
    for i in range(0, len(image)):
        if image[i][col] == 1:
            return True
    return False


def check_row(image: List[List[str]], row: int) -> bool:
    for i in range(0, len(image[0])):
        if image[row][i] == 1:
            return True
    return False


def find_left(image: List[List[str]], start, end, checker) -> bool:
    while start + 1 < end:
        mid = (start + end) // 2
        if checker(image, mid):
            end = mid
        else:
            left = mid
    if checker(image, start):
        return start
    return end


def find_right(image: List[List[str]], start, end, checker) -> bool:
    while start + 1 < end:
        mid = (start + end) // 2
        if checker(image, mid):
            start = mid
        else:
            end = mid
    if checker(image, end):
        return end
    return start


def min_area(image: List[List[str]], x: int, y: int) -> int:
    # write your code here
    if image is None or len(image) == 0 or len(image[0]) == 0:
        return 0

    n, m = len(image), len(image[0])
    left_col = find_left(image, 0, y, check_col)
    right_col = find_right(image, y, m - 1, check_col)
    top_row = find_left(image, 0, x, check_row)
    btm_row = find_right(image, x, n - 1, check_row)
    return (right_col - left_col + 1) * (btm_row - top_row + 1)


