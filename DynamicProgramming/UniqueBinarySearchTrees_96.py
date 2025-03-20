"""
LeetCode 96: https://leetcode.cn/problems/unique-binary-search-trees/description/
dp[3]，就是 元素1为头结点搜索树的数量 + 元素2为头结点搜索树的数量 + 元素3为头结点搜索树的数量
元素1为头结点搜索树的数量 = 右子树有2个元素的搜索树数量 * 左子树有0个元素的搜索树数量
元素2为头结点搜索树的数量 = 右子树有1个元素的搜索树数量 * 左子树有1个元素的搜索树数量
元素3为头结点搜索树的数量 = 右子树有0个元素的搜索树数量 * 左子树有2个元素的搜索树数量
有2个元素的搜索树数量就是dp[2]。
有1个元素的搜索树数量就是dp[1]。
有0个元素的搜索树数量就是dp[0]。
所以dp[3] = dp[2] * dp[0] + dp[1] * dp[1] + dp[0] * dp[2]
"""

class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        # dp[n]表示n有多少种二叉搜索树
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        # dp[3] = dp[0]*dp[2] + dp[1]*dp[1] + dp[2]*dp[0]
        # dp[n] = sum(i*dp[n-i-1])

        for i in range(3, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]

        return dp[n]