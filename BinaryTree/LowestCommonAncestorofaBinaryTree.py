"""
LeetCode 236: https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/
"""

from BinaryTree.TreeNode import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        # 如果找到了p或者q，就返回root, 表明找到了
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 如果左右都找到了，说明root就是最近公共祖先
        if left and right:
            return root
        # 如果左边没找到，右边找到了，说明最近公共祖先在右边
        elif not left and right:
            return right
        # 如果右边没找到，左边找到了，说明最近公共祖先在左边
        elif left and not right:
            return left


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    solution = Solution()
    p = root.left
    q = root.right
    print(solution.lowestCommonAncestor(root, p, q).val)  # 3
    p = root.left
    q = root.left.right.right
    print(solution.lowestCommonAncestor(root, p, q).val)  # 5
    p = root.left
    q = root.left.right.left
    print(solution.lowestCommonAncestor(root, p, q).val)  # 5
    p = root.left.left
    q = root.left.right.right
    print(solution.lowestCommonAncestor(root, p, q).val)  # 5
    p = root.left.left
    q = root.right.right
    print(solution.lowestCommonAncestor(root, p, q).val)  # 3
    p = root.left.left
    q = root.left
    print(solution.lowestCommonAncestor(root, p, q).val)  # 5
    p = root.left.right.right
    q = root.right.right
    print(solution.lowestCommonAncestor(root, p, q).val)  # 3
    p = root.left.right.right
    q = root.right
    print(solution.lowestCommonAncestor(root, p, q).val)  # 3
    p = root.left.right.right
    q = root.left.right.left
    print(solution.lowestCommonAncestor(root, p, q).val)  # 2
    p = root.left.right.right
    q = root.left.left
    print(solution.lowestCommonAncestor(root, p, q).val)  # 5
    p = root.left.right.right
    q = root.left
    print(solution.lowestCommonAncestor(root, p, q).val)  # 5