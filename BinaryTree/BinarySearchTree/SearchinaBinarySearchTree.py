"""
LeetCode 700: https://leetcode.cn/problems/search-in-a-binary-search-tree/description/
"""
from typing import Optional
from BinaryTree.TreeNode import TreeNode


# recursive
def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None
    if root.val == val:
        return root
    if root.val < val:
        return searchBST(root.right, val)
    if root.val > val:
        return searchBST(root.left, val)

# iterative
def searchBST2(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    while root:
        if root.val == val:
            return root
        elif root.val > val:
            root = root.left
        elif root.val < val:
            root = root.right