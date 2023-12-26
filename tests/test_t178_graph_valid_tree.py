# -*- coding: utf-8 -*-


import pytest
from bfs import _t178_graph_valid_tree as question


class TestT178GraphValidTree:

    @pytest.fixture
    def solution(self):
        return question.valid_tree

    def test_question_sample(self, solution):
        assert solution(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) is True

    def test_single_edge(self, solution):
        assert solution(2, [[1, 0]]) is True

    def test_edges_with_cycle_but_not_connected(self, solution):
        edges = [[0, 1], [9, 0], [8, 4], [8, 1], [4, 9], [2, 5], [5, 6], [7, 3]]
        assert solution(9, edges) is False
