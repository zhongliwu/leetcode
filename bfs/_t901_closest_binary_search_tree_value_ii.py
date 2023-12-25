# -*- coding: utf-8 -*-


from typing import (
    List,
)
from utils.Tree import TreeNode


def find_left_most(itr: TreeNode, stack: List[TreeNode]):
    while itr:
        stack.append(itr)
        itr = itr.left


def inorder_traversal(root: TreeNode, target: float):
    itr = root
    inorder_list, stack = [], []
    min_diff, min_idx = float('inf'), 0
    find_left_most(itr, stack)

    while stack:
        cur_node = stack.pop()
        inorder_list.append(cur_node.val)
        cur_diff = abs(cur_node.val - target)
        if cur_diff < min_diff:
            min_diff = cur_diff
            min_idx = len(inorder_list) - 1

        itr = cur_node.right
        find_left_most(itr, stack)

    return inorder_list, min_idx


"""
@param root: the given BST
@param target: the given target
@param k: the given k
@return: k values in the BST that are closest to the target
         we will sort your return value in output
"""


def closest_k_values(root: TreeNode, target: float, k: int) -> List[int]:
    inorder_list, min_idx = inorder_traversal(root, target)
    left, right = min_idx - 1, min_idx + 1
    result_list = [inorder_list[min_idx]]
    while (left > 0) and (right < len(inorder_list)) and (k >= 1):
        left_diff, right_diff = \
            abs(inorder_list[left] - target), \
            abs(inorder_list[right] - target)
        if left_diff < right_diff:
            result_list.append(inorder_list[left])
            left -= 1
        else:
            result_list.append(inorder_list[right])
            right += 1

        k -= 1

    while (k > 1) and (left >= 0):
        result_list.append(inorder_list[left])
        left -= 1
        k -= 1

    while (k > 1) and (right < len(inorder_list)):
        result_list.append(inorder_list[right])
        right += 1
        k -= 1

    return result_list
