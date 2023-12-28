# -*- coding: utf-8 -*-

from typing import (
    List,
)


def dfs(nums, permutation, permutations, visited):
    if len(permutation) == len(nums):
        permutations.append(permutation.copy())
        return

    for i in range(0, len(nums)):
        if visited[i]:
            continue
        if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
            continue
        permutation.append(nums[i])
        visited[i] = True
        dfs(nums, permutation, permutations, visited)
        visited[i] = False
        permutation[:] = permutation[: -1]


# @param nums: A list of integers
# @return: A list of unique permutations
#          we will sort your return value in output
def permute_unique(nums: List[int]) -> List[List[int]]:
    # write your code here
    permutations = []
    if nums is None:
        return permutations

    if len(nums) == 0:
        return [[]]

    visited = [False] * len(nums)
    nums.sort()
    dfs(nums, [], permutations, visited)
    return permutations

