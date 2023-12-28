# -*- coding: utf-8 -*-


from typing import (
    List,
)
from dfs.t816_traveling_salesman_problem import build_graph


def min_cost(n: int, roads: List[List[int]]):
    # Write your code here
    graph = build_graph(n, roads)
    # state = 1 << (n + 1)
    # f = [
    #     [int('inf')] * (n + 1)
    # ] * state
    # f[1][1] = 0
    # for i in range(1, state):
    pass
