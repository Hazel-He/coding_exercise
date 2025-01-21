"""
LeetCode 104: https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/
Can also use BFS to solve this problem.
Similar to 111. Minimum Depth of Binary Tree
"""


from typing import Optional
from BinaryTree.TreeNode import TreeNode


def maxDepth(root: Optional[TreeNode]) -> int:
    def dfs(root: Optional[TreeNode], depth: int):
        if not root:
            return depth
        return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

    return dfs(root, 0)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(maxDepth(root))  # Output is 3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(7)
    print(maxDepth(root))  # Output is 3
    root = TreeNode(1)
    print(maxDepth(root))  # Output is 1
    root = None
    print(maxDepth(root))  # Output is 0