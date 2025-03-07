"""
LeetCode 46: https://leetcode.cn/problems/permutations/description/
组合问题问题主要是用startIndex来解决，因为组合问题不需要考虑顺序，所以每次递归都从startIndex开始，这样就不会重复
排列问题主要用used数组，因为排列问题需要考虑顺序，所以每次递归都从0开始，但是需要一个used数组来记录哪些元素使用过了
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path.copy())
            for i in range(len(nums)):
                if used[i] == 1:
                    continue
                used[i] = 1
                path.append(nums[i])
                backtrack(path, used)
                used[i] = 0
                path.pop()

        backtrack([], [0]*len(nums))
        return res

