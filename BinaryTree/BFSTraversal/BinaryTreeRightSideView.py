"""
LeetCode 199: https://leetcode.cn/problems/binary-tree-right-side-view/description/
"""

from typing import Optional
from typing import List
from collections import deque
from BinaryTree.TreeNode import TreeNode


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    queue = deque([root])
    res = []
    while len(queue) > 0:
        layer_num = len(queue)
        while layer_num > 0:
            node = queue.popleft()
            if layer_num == 1:
                res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            layer_num -= 1
    return res


if __name__ == '__main__':
    print(rightSideView(None))  # []
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    print(rightSideView(root))  # [1, 3, 4]