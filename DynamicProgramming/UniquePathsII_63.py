"""
LeetCode 63: https://leetcode.cn/problems/unique-paths-ii/description/
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid) # row
        n = len(obstacleGrid[0]) # col
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        # init first dp row
        for i in range(1, n):
            if obstacleGrid[0][i] == 1 or dp[0][i-1] == 0:
                dp[0][i] = 0
            else:
                dp[0][i] = 1
        # init first dp col
        for j in range(1, m):
            if obstacleGrid[j][0] == 1 or dp[j-1][0] == 0:
                dp[j][0] = 0
            else:
                dp[j][0] = 1

        # start to loop
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]