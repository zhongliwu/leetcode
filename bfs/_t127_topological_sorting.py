# -*- coding: utf-8 -*-

from utils.Graph import DirectedGraphNode
import collections

"""
@param graph: A list of Directed graph node
@return: Any topological order for the given graph.
"""


def top_sort(graph):
    # write your code here
    nodes = collections.defaultdict(int)
    for elem in graph:
        if elem not in nodes:
            nodes[elem] = 0
        for n in elem.neighbors:
            nodes[n] += 1

    queue = collections.deque([])
    for n in nodes:
        if nodes[n] == 0:
            queue.append(n)

    topo_order = []
    while queue:
        cur_node = queue.popleft()
        topo_order.append(cur_node)
        for neighbor in cur_node.neighbors:
            nodes[neighbor] -= 1
            if nodes[neighbor] == 0:
                queue.append(neighbor)

    return topo_order