"""
LeetCode 226: https://leetcode.cn/problems/invert-binary-tree/description/
"""
from typing import Optional

from BinaryTree.TreeNode import TreeNode


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return root
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    print(invertTree(root))
    print(invertTree(root).left.val)  # Output is 7
    print(invertTree(root).right.val)  # Output is 2
    print(invertTree(root).left.left.val)  # Output is 9
    print(invertTree(root).left.right.val)  # Output is 6
    print(invertTree(root).right.left.val)  # Output is 3
    print(invertTree(root).right.right.val)  # Output is 1