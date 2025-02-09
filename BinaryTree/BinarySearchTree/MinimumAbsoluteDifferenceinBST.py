"""
LeetCode 530: https://leetcode.cn/problems/minimum-absolute-difference-in-bst/description/
"""


from typing import Optional
from BinaryTree.TreeNode import TreeNode


class Solution:
    pre = None
    minValue = float("inf")

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        self.getMinimumDifference(root.left)

        if self.pre and abs(self.pre.val - root.val) < self.minValue:
            self.minValue = abs(self.pre.val - root.val)
        self.pre = root

        self.getMinimumDifference(root.right)

        return self.minValue


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    solution = Solution()
    print(solution.getMinimumDifference(root))  # 1
    root = TreeNode(236)
    root.left = TreeNode(104)
    root.right = TreeNode(701)
    root.left.right = TreeNode(227)
    root.right.right = TreeNode(911)
    print(solution.getMinimumDifference(root))  # 9
    root = TreeNode(1)
    root.right = TreeNode(5)
    root.right.left = TreeNode(3)
    print(solution.getMinimumDifference(root))  # 2
    root = TreeNode(543)
    root.left = TreeNode(384)
    root.right = TreeNode(652)
    root.left.right = TreeNode(445)
    root.right.right = TreeNode(699)
    print(solution.getMinimumDifference(root))  # 47
    root = TreeNode(1)
    root.right = TreeNode(2)
    print(solution.getMinimumDifference(root))  # 1
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    print(solution.getMinimumDifference(root))  # 1
    root = TreeNode(1)
    root.left = TreeNode(1)
    print(solution.getMinimumDifference(root))  # 0
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    print(solution.getMinimumDifference(root))  # 0
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    print(solution.getMinimumDifference(root))  # 0
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(solution.getMinimumDifference(root))  # 1
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    print(solution.getMinimumDifference(root))  # 1
    root = TreeNode(1)
    root.left = TreeNode(5)
    root.right = TreeNode(3)
    print(solution.getMinimumDifference(root))  # 2
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(5)
    print(solution.getMinimumDifference(root))  # 2