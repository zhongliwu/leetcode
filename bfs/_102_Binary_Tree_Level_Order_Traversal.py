# -*- coding: utf-8 -*-

from typing import (
    List,
)
import collections
from utils import Tree


def level_order(root: Tree.TreeNode) -> List[List[int]]:
    if root is None:
        return []

    queue = collections.deque()
    queue.append(root)
    result = []
    while len(queue) > 0:
        result.append([elem for elem in queue])
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result





