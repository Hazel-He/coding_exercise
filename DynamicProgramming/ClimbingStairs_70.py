"""
LeetCode 70: https://leetcode.cn/problems/climbing-stairs/description/
1. 递推公式dp[i] = dp[i-1] + dp[i-2]
2. dp[i]的含义：到达第i阶楼梯的方法数
3. 初始化dp数组：dp = [0, 1, 2] 注意这里dp[0] = 0是没有任何含义的，只是为了方便dp[i]的含义和递推公式的统一
4. 遍历方向：从前往后
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0, 1, 2]
        # dp[i] = dp[i-1] + dp[i-2]
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[-1]
