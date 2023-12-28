# -*- coding: utf-8 -*-


from typing import (
    List,
)


class Result:
    def __init__(self):
        self.min_cost = int('inf')


def min_cost(n: int, roads: List[List[int]]) -> int:
    # Write your code here
    graph = build_graph(n, roads)
    result = Result()
    visited = {1}
    dfs(1, result, graph, visited, 0, n, [1])
    return result.min_cost


def dfs(start_city, result, graph, visited, cur_cost, n, path):
    if len(visited) == n:
        result.min_cost = min(result.min_cost, cur_cost)
        return

    for next_city in graph[start_city]:
        if next_city in visited:
            continue
        if has_better_path(next_city, path, graph):
            continue
        path.append(next_city)
        visited.add(next_city)
        dfs(next_city,
            result,
            graph,
            visited,
            cur_cost + graph[start_city][next_city],
            n,
            path)
        visited.remove(next_city)
        path.pop()


def has_better_path(city, path, graph):
    for i in range(1, len(path)):
        if graph[path[i - 1]][path[i]] + graph[path[-1]][city] > \
                graph[path[i - 1]][path[-1]] + graph[path[i]][city]:
            return True
    return False


def build_graph(n: int, roads: List[List[int]]) -> dict:
    graph = {
        i: {j: float('inf') for j in range(1, n + 1)}
        for i in range(1, n + 1)
    }
    for city_a, city_b, distance in roads:
        graph[city_a][city_b] = min(graph[city_a][city_b], distance)
        graph[city_b][city_a] = min(graph[city_b][city_a], distance)
    return graph
