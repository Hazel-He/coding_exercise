"""
LeetCode 538: https://leetcode.cn/problems/convert-bst-to-greater-tree/description/
Need the pre value to store the sum of the right subtree.
"""

from BinaryTree.TreeNode import TreeNode
from typing import Optional

class Solution:
    pre = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # right, mid, left
        if not root:
            return
        self.convertBST(root.right)
        root.val = root.val + self.pre
        self.pre = root.val
        self.convertBST(root.left)

        return root