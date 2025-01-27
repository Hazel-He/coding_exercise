"""
LeetCode 110: https://leetcode.cn/problems/balanced-binary-tree/description/
这个要每个子树都要判断高度，不能只算左右子树的高度看是否相差1，因为子树也可能不平衡，要一直递归判断
"""


from typing import Optional
from BinaryTree.TreeNode import TreeNode


def isBalanced(root: Optional[TreeNode]) -> bool:
    def getHeight(root):
        if not root:
            return 0
        left = getHeight(root.left)
        if left == -1:
            return -1
        right = getHeight(root.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        else:
            return max(left, right) + 1

    return False if getHeight(root) == -1 else True


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(isBalanced(root))  # Output is True
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)
    print(isBalanced(root))  # Output is False
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)
    print(isBalanced(root))  # Output is True
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(3)
    print(isBalanced(root))  # Output is True
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.right.left.left = TreeNode(4)
    print(isBalanced(root))  # Output is False
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.right.left.left = TreeNode(4)
    root.left.left.left.left = TreeNode(5)
    root.right.left.left.left = TreeNode(5)
    print(isBalanced(root))  # Output is False
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.right.right.right = TreeNode(4)
    print(isBalanced(root))  # Output is True
