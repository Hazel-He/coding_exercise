"""
LeetCode 513: https://leetcode.cn/problems/find-bottom-left-tree-value/description/
这题层序遍历是第一直觉，这里使用递归来做。
bottom left一定是最大深度的最左边的节点，所以递归的时候，先递归右子树，再递归左子树，这样最后递归到的节点就是最左边的节点。

用递归需要一个全局变量来记录最大深度，还有一个全局变量来记录结果。
这里全局变量可以用self来定义。
"""

from typing import Optional
from BinaryTree.TreeNode import TreeNode


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = 0
        self.res = root.val

        def traverse(root, depth):
            if not root.left and not root.right:  # 到了叶子节点
                if depth + 1 > self.maxDepth:
                    self.maxDepth = depth + 1
                    self.res = root.val
            if root.left:
                traverse(root.left, depth + 1)
            if root.right:
                traverse(root.right, depth + 1)

        traverse(root, 0)
        return self.res
