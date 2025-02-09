"""
LeetCode 98: https://leetcode.cn/problems/validate-binary-search-tree/description/
BST最重要的特性是使用中序遍历
BST的中序遍历是升序的，所以只要在中序遍历的过程中，判断当前节点的值是否大于前一个节点的值即可。
"""
from typing import Optional

from BinaryTree.TreeNode import TreeNode


class Solution:
    pre = None

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.isValidBST(root.left)
        if not left:
            return False
        if self.pre is not None and self.pre.val >= root.val:
            return False
        else:
            self.pre = root
        right = self.isValidBST(root.right)
        if not right:
            return False
        return True



if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    solution = Solution()
    print(solution.isValidBST(root))  # True
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    print(solution.isValidBST(root))  # False
    root = TreeNode(1)
    root.left = TreeNode(1)
    print(solution.isValidBST(root))  # False
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(20)
    print(solution.isValidBST(root))  # False
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(6)
    print(solution.isValidBST(root))  # True
    root = TreeNode(1)
    root.left = TreeNode(1)
    print(solution.isValidBST(root))  # False
    root = TreeNode(5)
    root.left = TreeNode(14)
    root.right = TreeNode(1)
    print(solution.isValidBST(root))  # False
    root = TreeNode(1)
    root.left = TreeNode(1)
    print(solution.isValidBST(root))  # False
    root = TreeNode(1)
    root.right = TreeNode(1)
    print(solution.isValidBST(root))  # False
    root = TreeNode(1)
    root.right = TreeNode(2)
    print(solution.isValidBST(root))  # True
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(solution.isValidBST(root))  # False
    root = TreeNode(1)
    root.left = TreeNode(1)
    print(solution.isValidBST(root))  # False
    root = TreeNode(1)
    root.right = TreeNode(1)
    print(solution.isValidBST(root))  # False
    root = TreeNode(1)
    root.right = TreeNode(2)
    print(solution.isValidBST(root))  # True
