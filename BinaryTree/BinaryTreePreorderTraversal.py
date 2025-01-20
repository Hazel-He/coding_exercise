"""
LeetCode 144: https://leetcode.cn/problems/binary-tree-preorder-traversal/description/
"""
from typing import Optional, List

from BinaryTree.TreeNode import TreeNode


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    def traverse(root, res):
        if root is None:
            return res
        res.append(root.val)
        traverse(root.left, res)
        traverse(root.right, res)
        return res

    return traverse(root, [])


def preorderTraversal2(root: Optional[TreeNode]) -> List[int]:
    # pre order is mid, left, right
    # put in stack order should be mid, right, left
    stack = []
    res = []
    stack.append(root)
    while len(stack) > 0:
        node = stack.pop()
        # handle leaf node
        if node is None:
            continue
        res.append(node.val)
        # first push left node, then right node
        stack.append(node.right)
        stack.append(node.left)

    return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(preorderTraversal(root))  # [1, 2, 3]
    root = None
    print(preorderTraversal(root))  # []
    root = TreeNode(1)
    print(preorderTraversal(root))  # [1]
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(preorderTraversal(root))  # [1, 2]
    root = TreeNode(1)
    root.right = TreeNode(2)
    print(preorderTraversal(root))  # [1, 2]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(preorderTraversal(root))  # [1, 2, 3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    print(preorderTraversal(root))  # [1, 2, 3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(3)
    print(preorderTraversal(root))  # [1, 2, 3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(preorderTraversal(root))  # [1, 2, 3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    print(preorderTraversal(root))  # [1, 2, 3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(preorderTraversal(root))  # [1, 2, 3, 4, 5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(preorderTraversal(root))  # [1, 2, 3, 4, 5, 6, 7]
