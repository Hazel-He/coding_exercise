"""
LeetCode 235: https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
这题与236题的区别在于，这题是二叉搜索树，所以可以根据节点值的大小关系来判断最近公共祖先在哪边
不需要像236题那样递归遍历所有的左右子树
"""

from BinaryTree.TreeNode import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val or root.val == q.val:
            return root
        if (root.val < p.val and root.val > q.val) or (root.val > p.val and root.val < q.val):
            return root
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)