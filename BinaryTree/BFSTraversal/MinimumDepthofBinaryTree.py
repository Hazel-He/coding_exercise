"""
LeetCode 111: https://leetcode.cn/problems/minimum-depth-of-binary-tree/description/
Can also use DFS to solve this problem.
Similar to 104. Maximum Depth of Binary Tree
I think BFS is more suitable, since for the shortest path, we don't need to traverse all nodes.
But for maximum depth, we need to traverse all nodes anyway, so DFS has lesser code and easier to think
"""
from collections import deque
from typing import Optional
from BinaryTree.TreeNode import TreeNode


def minDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    queue = deque([root])
    res = 0
    while len(queue) > 0:
        layer_count = len(queue)
        while layer_count > 0:
            node = queue.popleft()
            # If we find a leaf node, we can return the depth directly - 剪枝
            if not node.left and not node.right:
                return res + 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            layer_count -= 1
        res += 1
    return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(minDepth(root))  # Output is 2
    root = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)
    root.right.right.right.right = TreeNode(6)
    print(minDepth(root))  # Output is 5
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(minDepth(root))  # Output is 2
    root = TreeNode(1)
    print(minDepth(root))  # Output is 1
    root = None
    print(minDepth(root))  # Output is 0