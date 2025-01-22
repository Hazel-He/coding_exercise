"""
LeetCode 100: https://leetcode.cn/problems/same-tree/description/
"""
from typing import Optional
from BinaryTree.TreeNode import TreeNode


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    print(isSameTree(p, q))  # Output is True
    p = TreeNode(1)
    p.left = TreeNode(2)
    q = TreeNode(1)
    q.right = TreeNode(2)
    print(isSameTree(p, q))  # Output is False
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)
    q = TreeNode(1)
    q.left = TreeNode(1)
    q.right = TreeNode(2)
    print(isSameTree(p, q))  # Output is False
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(1)
    print(isSameTree(p, q))  # Output is True
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(1)
    q.left.left = TreeNode(3)
    print(isSameTree(p, q))  # Output is False
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(1)
    q.right.right = TreeNode(3)
    print(isSameTree(p, q))  # Output is False
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(1)
    q.left.right = TreeNode(3)
    print(isSameTree(p, q))  # Output is False
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(1)
    q.left.right = TreeNode(3)