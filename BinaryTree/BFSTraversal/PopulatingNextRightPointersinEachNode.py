"""
LeetCode 116: https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/description/
LeetCode 117: https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/description/
"""

from typing import Optional
from collections import deque
from BinaryTree.TreeNode import TreeNode


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: 'Optional[Node]') -> 'Optional[Node]':
    if not root:
        return root
    queue = deque([root])
    while len(queue) > 0:
        level_count = len(queue)
        while level_count > 0:
            node = queue.popleft()
            if level_count > 1:
                node.next = queue[0]
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            level_count -= 1
    return root


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(7)
    connect(root)
    print(root)
    print(root.left.next.val)  # Output is 3
    print(root.left.left.next.val)  # Output is 5
    print(root.left.right.next.val)  # Output is 7
