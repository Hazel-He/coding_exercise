"""
LeetCode 404: https://leetcode.cn/problems/sum-of-left-leaves/description/
"""
from typing import Optional

from BinaryTree.TreeNode import TreeNode


def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
    if not root or (not root.left and not root.right):
        return 0
    left = sumOfLeftLeaves(root.left)  # 遍历左子树
    if root.left and not root.left.left and not root.left.right:  # 特殊处理：左子树是左叶子的情况
        left = root.left.val
    right = sumOfLeftLeaves(root.right)  # 遍历右子树
    return left + right


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(sumOfLeftLeaves(root))  # Output is 24
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(sumOfLeftLeaves(root))  # Output is 11
    root = None
    print(sumOfLeftLeaves(root))  # Output is 0
    root = TreeNode(1)
    print(sumOfLeftLeaves(root))  # Output is 0
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(sumOfLeftLeaves(root))  # Output is 2
    root = TreeNode(1)
    root.right = TreeNode(2)
    print(sumOfLeftLeaves(root))  # Output is 0
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(sumOfLeftLeaves(root))  # Output is 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(sumOfLeftLeaves(root))  # Output is 4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    print(sumOfLeftLeaves(root))  # Output is 4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print(sumOfLeftLeaves(root))  # Output is 4
