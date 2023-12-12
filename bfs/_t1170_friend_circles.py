# -*- coding: utf-8 -*-

import collections
from typing import (
    List,
)


def find_circle_num(m: List[List[int]]) -> int:
    if (m is None) or (len(m) == 0) or (len(m) != len(m[0])):
        return 0

    visited = set()
    num_of_circles = 0
    col, row, N = 0, 0, len(m)
    for i in range(0, N):
        for j in range(0, N):
            cur_tuple = (i, j)
            if cur_tuple in visited:
                continue

            if m[i][j] == 1:
                num_of_circles += 1
                search(i, j, m, visited, N)

    return num_of_circles


def search(i: int, j: int, m: List[List[int]], visited: set, N: int):
    queue = collections.deque()
    queue.append((i, j))
    while queue:
        cur_pos = queue.popleft()
        row, col = cur_pos[0], cur_pos[1]
        visited.add((row, col))
        visited.add((col, row))

        for itr in range(0, N):
            if m[row][itr] == 1 and (row, itr) not in visited:
                queue.append((row, itr))

        for itr in range(0, N):
            if m[itr][col] == 1 and (itr, col) not in visited:
                queue.append((itr, col))
