# -*- coding: utf-8 -*-


from utils import (
    Tree as tr
)


def subtree_sum(root):
    if root is None:
        return 0, float('-inf'), None

    if root.left is None and root.right is None:
        return root.val, root.val, root

    left_sum, left_max_sum, left_max_node = subtree_sum(root.left)
    right_sum, right_max_sum, right_max_node = subtree_sum(root.right)
    node_sum = left_sum + right_sum + root.val
    max_sum = max(left_max_sum, right_max_sum, node_sum)
    if max_sum == left_max_sum:
        return node_sum, left_max_sum, left_max_node

    if max_sum == right_max_sum:
        return node_sum, right_max_sum, right_max_node

    return node_sum, node_sum, root


def find_subtree(root: tr.TreeNode) -> tr.TreeNode:
    root_sum, max_sum, max_node = subtree_sum(root)
    return max_node

