# -*- coding: utf-8 -*-

import pytest
from bfs import _t901_closest_binary_search_tree_value_ii as question
from utils.Tree import TreeNode
from utils.ArrayUtils import compare_arr


class TestT901ClosestBinarySearchTreeValueII:

    @pytest.fixture
    def solution(self):
        return question.closest_k_values

    def test_one_node(self, solution):
        root = TreeNode(2)
        node_list = solution(root, 1.375, 1)
        assert compare_arr(node_list, [2])

    def test_sample(self, solution):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        node_list = solution(root, 0.275000, 2)
        assert compare_arr(node_list, [1, 2])

    def test_three_node(self, solution):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        node_list = solution(root, 5.571429, 2)
        assert compare_arr(node_list, [2, 3])

    def test_consecutive_number(self, solution):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)
        root.left.left = TreeNode(2)
        root.left.left.left = TreeNode(1)
        root.left.right = TreeNode(4)
        node_list = solution(root, 2.857143, 4)
        assert compare_arr(node_list, [1, 2, 3, 4])
