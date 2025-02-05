"""
LeetCode 617: https://leetcode.cn/problems/merge-two-binary-trees/description/
"""

from typing import Optional
from BinaryTree.TreeNode import TreeNode


def mergeTrees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root1:
        return root2
    if not root2:
        return root1
    left = mergeTrees(root1.left, root2.left)
    right = mergeTrees(root1.right, root2.right)
    return TreeNode(root1.val + root2.val, left, right)


