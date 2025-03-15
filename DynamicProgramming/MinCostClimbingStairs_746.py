"""
LeetCode 746: https://leetcode.cn/problems/min-cost-climbing-stairs/description/
"""
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0, 0]
        for i in range(2, len(cost) + 1):
            dp.append(min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1]))
        return dp[-1]
