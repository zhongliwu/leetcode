# -*- coding: utf-8 -*-

from typing import (
    List,
)
import collections


def valid_node(n: int, node: int) -> bool:
    if (node < 0) or (node >= n):
        return False
    return True


"""
@param n: An integer
@param edges: a list of undirected edges
@return: true if it's a valid tree, or false
"""


def valid_tree(n: int, edges: List[List[int]]) -> bool:
    # write your code here
    if n <= 0:
        return True

    if len(edges) <= 0:
        return False

    if len(edges) != n - 1:
        return False

    adjacent_list = collections.defaultdict(list)
    for elem in edges:
        if not valid_node(n, elem[0]) or not valid_node(n, elem[1]):
            return False

        adjacent_list[elem[0]].append(elem[1])
        adjacent_list[elem[1]].append(elem[0])

    queue = collections.deque()
    queue.append(0)
    visited = set()
    visited.add(0)
    while queue:
        cur_node = queue.popleft()
        for elem in adjacent_list[cur_node]:
            if elem in visited:
                continue
            queue.append(elem)
            visited.add(elem)

    if len(visited) != n:
        return False

    return True
