"""
LeetCode 509: https://leetcode.cn/problems/fibonacci-number/description/
DP要确认的是：
1. dp数组的定义
2. dp数组的初始化
3. dp数组的递推公式
4. dp数组的遍历方向
"""


class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        dp = [0, 1]
        for i in range(2, n + 1):
            dp.append(dp[i - 2] + dp[i - 1])

        return dp[-1]
