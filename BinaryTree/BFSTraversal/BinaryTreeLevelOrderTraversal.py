"""
LeetCode 102: https://leetcode.cn/problems/binary-tree-level-order-traversal/description/
1. 在python中，如果要用queue，最好是使用deque，deque的底层是双向链表，所以pop(0)的时间复杂度是O(1)，list底层是array，pop(0)的时间复杂度是O(n)， stack可以用list
2. BFS通常使用queue
"""
from typing import Optional
from typing import List
from collections import deque
from BinaryTree.TreeNode import TreeNode


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []
    queue = deque()
    res = []
    queue.append(root)
    while len(queue) > 0:
        # now the queue only has one layer node, so mark the size of the layer
        size = len(queue)
        layer_result = []
        while size > 0:
            node = queue.popleft()
            layer_result.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            size -= 1
        res.append(layer_result)
    return res


if __name__ == '__main__':
    print(levelOrder(None))  # []
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(levelOrder(root))  # [[3], [9, 20], [15, 7]]