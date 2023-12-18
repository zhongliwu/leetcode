# -*- coding: utf-8 -*-

import pytest
from bfs import _t628_maximum_subtree as question
from utils import Tree as tr


class TestT628MaximumSubtree:

    @pytest.fixture
    def solution(self):
        return question.find_subtree

    def test_sample(self, solution):
        root = tr.TreeNode(1)
        root.left = tr.TreeNode(-5)
        root.right = tr.TreeNode(2)
        root.left.left = tr.TreeNode(0)
        root.left.right = tr.TreeNode(3)
        root.right.left = tr.TreeNode(-4)
        root.right.right = tr.TreeNode(-5)
        solution(root)

