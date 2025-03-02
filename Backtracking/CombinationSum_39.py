"""
LeetCode 39: https://leetcode.cn/problems/combination-sum/description/
注意combination不要有重复，所以在backtrack的时候，传入的candidates是candidates[i:]，而不是candidates
比如2367，第一个选2，后面都是2367
但是第一个选3，后面就是367，不会有2了
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(candidates, combination):
            if sum(combination) > target:  #剪枝，也可以放在for循环里面
                return
            if sum(combination) == target:
                res.append(combination.copy())
                return
            for i in range(len(candidates)):
                combination.append(candidates[i])
                backtrack(candidates[i:], combination)
                combination.pop()

        backtrack(candidates, [])
        return res
