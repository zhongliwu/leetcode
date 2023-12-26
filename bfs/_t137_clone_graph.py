# -*- coding: utf-8 -*-

from utils.Graph import UndirectedGraphNode
import collections

"""
Definition for a UndirectedGraphNode:
class UndirectedGraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = []
"""


def find_nodes(node: UndirectedGraphNode):
    queue = collections.deque()
    queue.append(node)
    visited = set()
    while queue:
        cur_node = queue.popleft()
        visited.add(cur_node)
        for n in cur_node.neighbors:
            if n not in visited:
                visited.add(n)
                queue.append(n)

    return visited


def copy_nodes(node_list):
    mapping = {}
    for node in node_list:
        mapping[node] = UndirectedGraphNode(node.label)
    return mapping


def copy_edges(node_mapping):
    for elem in node_mapping:
        new_node = node_mapping[elem]
        new_node.neighbors = []
        for neighbor in elem.neighbors:
            new_node.neighbors.append(node_mapping[neighbor])


"""
@param node: A undirected graph node
@return: A undirected graph node
"""
def clone_graph(node: UndirectedGraphNode) -> UndirectedGraphNode:
    # write your code here
    if node is None:
        return None

    node_list = find_nodes(node)
    node_mapping = copy_nodes(node_list)
    copy_edges(node_mapping)

    return node_mapping[node]




