"""
LeetCode 145: https://leetcode.cn/problems/binary-tree-postorder-traversal/description/
"""

from typing import Optional, List

from BinaryTree.TreeNode import TreeNode


def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    def traverse(root, res):
        if root is None:
            return res
        traverse(root.left, res)
        traverse(root.right, res)
        res.append(root.val)
        return res

    return traverse(root, [])


def postorderTraversal2(root: Optional[TreeNode]) -> List[int]:
    # post order is left, right, mid
    # before reverse the order should be mid, right, left
    # then reverse the res list, get the result
    stack = []
    res = []
    stack.append(root)
    while len(stack) > 0:
        node = stack.pop()
        # handle leaf
        if node is None:
            continue
        res.append(node.val)
        stack.append(node.left)
        stack.append(node.right)

    # reverse the result
    res.reverse()
    return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(postorderTraversal(root))  # [3, 2, 1]
    root = None
    print(postorderTraversal(root))  # []
    root = TreeNode(1)
    print(postorderTraversal(root))  # [1]
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(postorderTraversal(root))  # [2, 1]
    root = TreeNode(1)
    root.right = TreeNode(2)
    print(postorderTraversal(root))  # [2, 1]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(postorderTraversal(root))  # [2, 3, 1]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    print(postorderTraversal(root))  # [3, 2, 1]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(3)
    print(postorderTraversal(root))  # [3, 2, 1]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(postorderTraversal(root))  # [3, 2, 1]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    print(postorderTraversal(root))  # [3, 2, 1]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(postorderTraversal(root))  # [2, 4, 5, 3, 1]
