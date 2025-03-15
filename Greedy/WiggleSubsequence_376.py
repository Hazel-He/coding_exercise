"""
LeetCode 376: https://leetcode.cn/problems/wiggle-subsequence/description/
"""

from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        change = 0  # change定义的是波动的次数，所以初始值为0
        prediff = 0
        for i in range(1, len(nums)):  # 题目有说1 <= nums.length, 如果nums长度为1，那么不会进入循环
            diff = nums[i] - nums[i - 1]
            if abs(diff) > 0 and prediff == 0:
                prediff = diff
                change += 1
                continue
            if diff > 0 > prediff or diff < 0 and prediff > 0:
                prediff = diff
                change += 1

        return change + 1  # 子序列的长度是波动次数+1
