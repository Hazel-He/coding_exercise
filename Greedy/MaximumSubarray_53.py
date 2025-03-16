"""
LeetCode 53: https://leetcode.cn/problems/maximum-subarray/description/
贪心贪的是哪里呢？
如果 -2 1 在一起，计算起点的时候，一定是从 1 开始计算，因为负数只会拉低总和，这就是贪心贪的地方！
局部最优：当前“连续和”为负数的时候立刻放弃，从下一个元素重新计算“连续和”，因为负数加上下一个元素 “连续和”只会越来越小。
全局最优：选取最大“连续和”
局部最优的情况下，并记录最大的“连续和”，可以推出全局最优。
所以区间终止位置靠记录最大的“连续和”来获得
比如：-2 1 -3 4 -1 2 1 -5 4
-2 先被抛弃
1 -3 = -2 再次被抛弃，从4开始
4 -1 2 1 = 6，此时会记录最大的“连续和”为6
所以当遍历到-5的时候，连续和仍然是4 -1 2 1 -5 = 1，但不会更新最大的“连续和”
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float("-inf")
        subSum = 0

        for num in nums:
            if subSum < 0:
                subSum = num
            else:
                subSum += num
            result = max(subSum, result)

        return result
