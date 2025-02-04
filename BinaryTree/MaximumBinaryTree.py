"""
LeetCode 654: https://leetcode.cn/problems/maximum-binary-tree/description/
"""


from typing import List, Optional
from BinaryTree.TreeNode import TreeNode


def constructMaximumBinaryTree(nums: List[int]) -> Optional[TreeNode]:
    if len(nums) == 1:
        return TreeNode(nums[0], None, None)
    max_value = float("-inf")
    max_value_idx = 0
    for idx, value in enumerate(nums):
        if value > max_value:
            max_value = value
            max_value_idx = idx

    left = None if max_value_idx == 0 else constructMaximumBinaryTree(nums[:max_value_idx])
    right = None if max_value_idx == len(nums) - 1 else constructMaximumBinaryTree(nums[max_value_idx + 1:])
    return TreeNode(max_value, left, right)


def printTree(root: Optional[TreeNode]):
    if not root:
        return
    print(root.val, end=" ")
    printTree(root.left)
    printTree(root.right)


if __name__ == '__main__':
    nums = [3, 2, 1, 6, 0, 5]
    root = constructMaximumBinaryTree(nums)
    printTree(root)  # Output is [6, 3, 5, None, 2, 0, None, None, 1]
    print("")
    nums = [3, 2, 1]
    root = constructMaximumBinaryTree(nums)
    printTree(root)  # Output is [3, None, 2, None, 1]
    print("")
    nums = [3, 2]
    root = constructMaximumBinaryTree(nums)
    printTree(root)  # Output is [3, None, 2]
    print("")
    nums = [3]
    root = constructMaximumBinaryTree(nums)
    printTree(root)  # Output is [3]
