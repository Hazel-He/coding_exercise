"""
LeetCode 637: https://leetcode.cn/problems/average-of-levels-in-binary-tree/description/
"""

from typing import Optional
from typing import List
from collections import deque
from BinaryTree.TreeNode import TreeNode


def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
    queue = deque([root])
    res = []
    while len(queue) > 0:
        level_count = len(queue)
        level_nums = []
        while level_count > 0:
            node = queue.popleft()
            level_nums.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            level_count -= 1
        res.append(sum(level_nums) / len(level_nums))
    return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(averageOfLevels(root))  # Output is [3.0, 14.5, 11.0]