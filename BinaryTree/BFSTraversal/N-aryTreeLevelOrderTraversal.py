"""
LeetCode 429: https://leetcode.cn/problems/n-ary-tree-level-order-traversal/description/
"""

from typing import List, Optional
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


def levelOrder(root: 'Node') -> List[List[int]]:
    if not root:
        return []
    queue = deque([root])
    res = []
    while len(queue) > 0:
        level_count = len(queue)
        level_nums = []
        while level_count > 0:
            node = queue.popleft()
            level_nums.append(node.val)
            if node.children:
                for node_child in node.children:
                    if node_child:
                        queue.append(node_child)
            level_count -= 1
        res.append(level_nums)
    return res


if __name__ == '__main__':
    root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
    print(levelOrder(root))  # Output is [[1], [3, 2, 4], [5, 6]]
