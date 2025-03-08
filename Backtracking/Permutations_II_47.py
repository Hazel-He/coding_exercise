"""
LeetCode 47: https://leetcode.cn/problems/permutations-ii/description/
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path.copy())
            i = 0
            while i < len(nums):
                if used[i] == 1:
                    i += 1
                    continue
                used[i] = 1
                path.append(nums[i])
                backtrack(path, used)
                used[i] = 0
                path.pop()
                while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                    i = i + 1
                    continue
                i += 1

        backtrack([], [0] * len(nums))
        return res
