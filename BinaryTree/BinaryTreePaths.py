"""
LeetCode 257: https://leetcode.cn/problems/binary-tree-paths/description/
注意回溯的用法
"""

from typing import Optional, List
from BinaryTree.TreeNode import TreeNode


def binaryTreePaths(root: Optional[TreeNode]) -> List[str]:
    def traverse(root, path, res):
        path.append(str(root.val))
        if not root.left and not root.right:
            res.append("->".join(path))
            return res
        if root.left:
            traverse(root.left, path, res)
            path.pop()
        if root.right:
            traverse(root.right, path, res)
            path.pop()
        return res

    return traverse(root, [], [])

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    print(binaryTreePaths(root))  # ["1->2->5", "1->3"]
    root = TreeNode(1)
    print(binaryTreePaths(root))  # ["1"]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(binaryTreePaths(root))  # ["1->2->4", "1->2->5", "1->3->6", "1->3->7"]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print(binaryTreePaths(root))  # ["1->2->4", "1->2->5", "1->3->6"]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(11)
    root.right.left.left = TreeNode(12)
    root.right.left.right = TreeNode(13)
    root.right.right.left = TreeNode(14)
    root.right.right.right = TreeNode(15)
    print(binaryTreePaths(root))  # ["1->2->4->8", "1->2->4->9", "1->2->5->10", "1->2->5->11", "1->3->6->12", "1->3->6->13", "1->3->7->14", "1->3->7->15"]
