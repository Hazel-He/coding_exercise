"""
LeetCode 112: https://leetcode.cn/problems/path-sum/description/
"""

from typing import Optional
from BinaryTree.TreeNode import TreeNode


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False

    def traverse(root, pathSum):
        print(root.val)
        pathSum += root.val
        if not root.left and not root.right:
            if pathSum == targetSum:
                return True
            return False
        if root.left:
            if traverse(root.left, pathSum):
                return True
        if root.right:
            if traverse(root.right, pathSum):
                return True
        return False

    return traverse(root, 0)


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    print(hasPathSum(root, 22))  # Output is True
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(hasPathSum(root, 0))  # Output is False
    root = None
    print(hasPathSum(root, 0))  # Output is False
    root = TreeNode(1)
    print(hasPathSum(root, 1))  # Output is True
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(hasPathSum(root, 1))  # Output is False
    root = TreeNode(1)
    root.right = TreeNode(2)
    print(hasPathSum(root, 1))  # Output is False
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(hasPathSum(root, 3))  # Output is True
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(hasPathSum(root, 8))  # Output is True
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    print(hasPathSum(root, 8))  # Output is False
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    print(hasPathSum(root, 7))  # Output is True
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    print(hasPathSum(root, 6))  # Output is False