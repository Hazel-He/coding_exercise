"""
LeetCode 101: https://leetcode.cn/problems/symmetric-tree/description/
"""


from typing import Optional
from BinaryTree.TreeNode import TreeNode


def isSymmetric(root: Optional[TreeNode]) -> bool:
    def checkLeftRight(left: Optional[TreeNode], right: Optional[TreeNode]):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return checkLeftRight(left.left, right.right) and checkLeftRight(left.right, right.left)

    return checkLeftRight(root.left, root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print(isSymmetric(root))  # Output is True
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)
    print(isSymmetric(root))  # Output is False
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(2)
    root.right.left = TreeNode(2)
    print(isSymmetric(root))  # Output is False
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(3)
    print(isSymmetric(root))  # Output is False
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)
    print(isSymmetric(root))  # Output is True
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(4)
    print(isSymmetric(root))  # Output is True
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(5)
    root.right.left.left = TreeNode(5)
    print(isSymmetric(root))  # Output is True
