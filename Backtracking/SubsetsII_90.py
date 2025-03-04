"""
LeetCode 90: https://leetcode.cn/problems/subsets-ii/description/
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        def backtrack(start, combination):
            res.append(combination.copy())
            if start >= len(nums):
                return
            i = start
            while i < len(nums):
                combination.append(nums[i])
                backtrack(i + 1, combination)
                combination.pop()
                while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                    i += 1
                i += 1

        backtrack(0, [])
        return res
