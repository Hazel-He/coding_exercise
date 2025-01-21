"""
LeetCode 107: https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/description/

The only difference between this problem and BinaryTreeLevelOrderTraversal.py is that we need to reverse the result list at the end.
"""
from typing import Optional
from typing import List
from collections import deque
from BinaryTree.TreeNode import TreeNode

def levelOrderBottom(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    queue = deque([root])
    res = []
    while len(queue) > 0:
        size = len(queue)
        layer_result = []
        while size > 0:
            node = queue.popleft()
            layer_result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            size -= 1
        res.append(layer_result)
    res.reverse()
    return res


if __name__ == '__main__':
    print(levelOrderBottom(None))  # []
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(levelOrderBottom(root))  # [[15, 7], [9, 20], [3]]