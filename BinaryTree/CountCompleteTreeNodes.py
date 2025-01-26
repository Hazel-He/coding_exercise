"""
LeetCode 222: https://leetcode.cn/problems/count-complete-tree-nodes/description/
可以用普通二叉树的求法
但是这里是完全二叉树，所以可以利用完全二叉树性质的求法

在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2^(h-1)  个节点。

完全二叉树只有两种情况，情况一：就是满二叉树，情况二：最后一层叶子节点没有满。

对于情况一，可以直接用 2^树深度 - 1 来计算，注意这里根节点深度为1。

对于情况二，分别递归左孩子，和右孩子，递归到某一深度一定会有左孩子或者右孩子为满二叉树，然后依然可以按照情况1来计算。
"""
from typing import Optional

from BinaryTree.TreeNode import TreeNode


def countNodes(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    left_count, right_count = 0, 0
    left, right = root.left, root.right  # 这里初始为0是有目的的，为了下面求指数方便
    while left:  # 求左子树深度
        left = left.left
        left_count += 1
    while right:  # 求右子树深度
        right = right.right
        right_count += 1
    if left_count == right_count:
        return (2 << left_count) - 1  # 2<<2 = 8, 相当于2^3，所以leftDepth初始为0

    return countNodes(root.left) + countNodes(root.right) + 1


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    print(countNodes(root))  # Output is 6
    root = None
    print(countNodes(root))  # Output is 0
    root = TreeNode(1)
    print(countNodes(root))  # Output is 1
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(countNodes(root))  # Output is 2
    root = TreeNode(1)
    root.right = TreeNode(2)
    print(countNodes(root))  # Output is 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(countNodes(root))  # Output is 3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print(countNodes(root))  # Output is 4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    print(countNodes(root))  # Output is 4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(countNodes(root))  # Output is 7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    print(countNodes(root))  # Output is 8
