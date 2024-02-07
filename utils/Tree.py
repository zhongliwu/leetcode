# -*- coding: utf-8 -*-


import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def serialize(root):
    # write your code here
    if root is None:
        return '{}'

    queue = collections.deque()
    queue.append(root)
    idx = 0
    while idx < len(queue):
        cur = queue[idx]
        if cur:
            queue.append(cur.left)
            queue.append(cur.right)
        idx += 1

    while queue[-1] is None:
        queue.pop()

    return '{%s}' % ','.join([
        str(node.val) if node is not None else '#' for node in queue
    ])


def deserialize(data):
    # write your code here
    if data == '{}':
        return None

    values = data[1: -1].split(',')
    root = TreeNode(int(values[0]))
    is_left = True
    idx = 0
    queue = collections.deque()
    queue.append(root)
    for i in range(1, len(values)):
        if values[i] != '#':
            node = TreeNode(int(values[i]))
            queue.append(node)
            if is_left:
                queue[idx].left = node
            else:
                queue[idx].right = node

        if not is_left:
            idx += 1

        is_left = not is_left

    return root
