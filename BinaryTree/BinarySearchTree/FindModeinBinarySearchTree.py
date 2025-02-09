"""
LeetCode 501: https://leetcode.cn/problems/find-mode-in-binary-search-tree/description/
"""
from typing import Optional
from typing import List
from BinaryTree.TreeNode import TreeNode


class Solution:
    max_freq = 0
    cur_freq = 0
    res = []
    pre = None

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        # 左
        self.findMode(root.left)

        # 中
        if self.pre:
            # 更新cur_freq
            if self.pre.val == root.val:
                self.cur_freq += 1
            else:
                self.cur_freq = 1

            # 更新max_freq和res
            if self.cur_freq == self.max_freq:
                self.res.append(root.val)
            elif self.cur_freq > self.max_freq:
                self.max_freq = self.cur_freq
                self.res = [root.val]
        else:
            # 第一个节点，记得必须初始化所有的值
            self.cur_freq = 1
            self.res = [root.val]
            self.max_freq = 1
        # 更新pre值
        self.pre = root

        # 右
        self.findMode(root.right)

        return self.res


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)
    solution = Solution()
    print(solution.findMode(root))  # [2]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(2)
    print(solution.findMode(root))  # [2]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(3)
    print(solution.findMode(root))  # [2]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(3)
    print(solution.findMode(root))  # [3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    print(solution.findMode(root))  # [1, 2, 3, 4]
    root = TreeNode(1)
    root.right = TreeNode(1)
    print(solution.findMode(root))  # [1]
    root = TreeNode(1)
    root.left = TreeNode(1)
    print(solution.findMode(root))  # [1]
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    print(solution.findMode(root))  # [1]
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    print(solution.findMode(root))  # [1]
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(2)
    print(solution.findMode(root))  # [1, 2]
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)
    print(solution.findMode(root))  # [1, 2]
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)
    print(solution.findMode(root))  # [1, 2]
