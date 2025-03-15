"""
LeetCode 62: https://leetcode.cn/problems/unique-paths/description/
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j]: the number of possible unique paths that the robot can take to reach [i,j]
        # 第一行和第一列只有一种走法，所以第一行和第一列都是1
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
