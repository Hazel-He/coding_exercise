"""
LeetCode 515: https://leetcode.cn/problems/find-largest-value-in-each-tree-row/description/
"""

from typing import Optional
from typing import List
from collections import deque
from BinaryTree.TreeNode import TreeNode


def largestValues(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    queue = deque([root])
    res = []
    while len(queue) > 0:
        row_count = len(queue)
        row_largest_num = float("-inf")
        while row_count > 0:
            node = queue.popleft()
            row_largest_num = max(node.val, row_largest_num)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            row_count -= 1
        res.append(row_largest_num)
    return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(9)
    print(largestValues(root))  # Output is [1, 3, 9]