# -*- coding: utf-8 -*-

from typing import (
    List,
)


def dfs(results: List[List[int]], sub_set: List[int], start_idx: int, nums: List[int]):
    results.append(sub_set)
    for i in range(start_idx, len(nums)):
        new_sub_set = sub_set.copy()
        new_sub_set.append(nums[i])
        dfs(results, new_sub_set, i + 1, nums)

# TODO: python's recursion seems to have a problem in this case, need to be reviewed later
# def dfs_ii(results: List[List[int]], sub_set: List[int], start_idx: int, nums: List[int]):
#     if start_idx == len(nums):
#         results.append(sub_set.copy())
#         return
#
#     sub_set.append(nums[start_idx])
#     dfs_ii(results, sub_set, start_idx + 1, nums)
#     sub_set = sub_set[: -1]
#     dfs_ii(results, sub_set, start_idx + 1, nums)


"""
@param nums: A set of numbers
@return: A list of lists
         we will sort your return value in output
"""


def subsets(nums: List[int]) -> List[List[int]]:
    # write your code here
    if nums is None:
        return []

    nums.sort()
    results = []
    sub_set = []
    dfs(results, sub_set, 0, nums)
    return results
