"""
LeetCode 113: https://leetcode.cn/problems/path-sum-ii/description/

这里有几个小坑：
1. 递归里面自带回溯，之前把pathSum把sum当参数传进去，是隐式的回溯，先加value，完成后减value。这里不能使用隐式，因为list是引用传递，无法隐式，list会一直变化，所以需要显式回溯，先加value，完成后pop。
2. 由于path是引用传递，所以不能直接append，需要deepcopy一份，否则即使加入，也会因为后面的pop而value消失。
"""
from typing import Optional
from typing import List
from BinaryTree.TreeNode import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        self.res = []
        def traverse(root, path):
            path.append(root.val)
            if not root.left and not root.right:
                if sum(path) == targetSum:
                    self.res.append([i for i in path])
            if root.left:
                traverse(root.left, path)
                path.pop()
            if root.right:
                traverse(root.right, path)
                path.pop()
        traverse(root, [])
        return self.res

if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    print(Solution().pathSum(root, 22))  # Output is [[5, 4, 11, 2], [5, 8, 4, 5]]
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(Solution().pathSum(root, 0))  # Output is []
    root = None
    print(Solution().pathSum(root, 0))  # Output is []
    root = TreeNode(1)
    print(Solution().pathSum(root, 1))  # Output is [[1]]
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(Solution().pathSum(root, 1))  # Output is []
    root = TreeNode(1)
    root.right = TreeNode(2)
    print(Solution().pathSum(root, 1))  # Output is []
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().pathSum(root, 3))  # Output is [[1, 2]]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(Solution().pathSum(root, 3))  # Output is [[1, 2]]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print(Solution().pathSum(root, 3))  # Output is [[1, 2]]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode