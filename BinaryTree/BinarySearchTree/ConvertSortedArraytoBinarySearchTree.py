"""
LeetCode 108: https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/
"""

from typing import List, Optional
from BinaryTree.TreeNode import TreeNode

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root