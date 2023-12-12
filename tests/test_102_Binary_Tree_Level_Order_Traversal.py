# -*- coding: utf-8 -*-

import pytest
from bfs import _102_Binary_Tree_Level_Order_Traversal as question
from utils import Tree


class Test102BinaryTreeLevelOrderTraversal:
    @pytest.fixture
    def solution(self):
        return question.level_order

    def test_empty(self, solution):
        root = None
        assert len(solution(root)) == 0

    def test_two_level_full(self, solution):
        root = Tree.TreeNode(1)
        root.left = Tree.TreeNode(2)
        root.right = Tree.TreeNode(3)
        solution(root)
