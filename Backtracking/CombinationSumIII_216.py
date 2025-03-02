"""
LeetCode 216: https://leetcode.cn/problems/combination-sum-iii/description/
"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(start, combination):
            if len(combination) == k:
                if sum(combination) == n:
                    res.append(combination.copy())
                return

            for i in range(start, 9-(k-len(combination))+2):
                combination.append(i)
                backtrack(i+1, combination)
                combination.pop()

        backtrack(1,[])
        return res