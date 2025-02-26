"""
LeetCode 669: https://leetcode.cn/problems/trim-a-binary-search-tree/description/
"""

from BinaryTree.TreeNode import TreeNode
from typing import Optional
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root