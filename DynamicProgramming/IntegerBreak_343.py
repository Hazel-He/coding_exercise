"""
LeetCode 343: https://leetcode.cn/problems/integer-break/description/
第一步定义dp数组：dp[i]表示数字i拆分后的最大乘积
第二步初始化dp数组：
dp[0]=0, dp[1]=0 (这两个不会用到), dp[2] = 1
第二步定义递推公式：
以10为例子：
10 = 1 + 9 -> 结果是1*9 or 1*(dp[9]): 意思要么10拆分成1和9，要么接着拆分9，取乘积的最大值
10 = 2 + 8 -> 结果是2*8 or 2*(dp[8])
其他同上
对于每一个拆分j，要取max(j * (i - j), j * dp[i - j])
因为要loop不同的j，所以还要跟之前的dp[i]比较，取最大值
所以递推公式是：dp[i] = max(j * (i - j), j * dp[i - j], dp[i])
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i]: 正整数i可以拆分的最大乘积
        dp = [0] * (n + 1)
        # 初始化dp数组 dp[0]=0, dp[1]=0 (这两个不会用到), dp[2] = 1
        dp[2] = 1
        # 递推公式
        for i in range(3, n + 1):
            # j不用到i，因为i拆分成两个数，最大的数是i//2
            for j in range(1, i // 2 + 1):
                dp[i] = max(j * (i - j), j * dp[i - j], dp[i])

        return dp[n]
