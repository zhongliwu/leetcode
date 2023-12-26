# -*- coding: utf-8 -*-


class UndirectedGraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = []


class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
