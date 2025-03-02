"""
LeetCode 40: https://leetcode.cn/problems/combination-sum-ii/description/
都知道组合问题可以抽象为树形结构，那么“使用过”在这个树形结构上是有两个维度的，一个维度是同一树枝上使用过，一个维度是同一树层上使用过。
那么问题来了，我们是要同一树层上使用过，还是同一树枝上使用过呢？
回看一下题目，元素在同一个组合内是可以重复的，怎么重复都没事，但两个组合不能相同。
所以我们要去重的是同一树层上的“使用过”，同一树枝上的都是一个组合里的元素，不用去重。

树层去重的话，需要对数组排序！不然使用used数组或set很容易跟同一树枝弄混
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtack(start, combination):
            if sum(combination) > target:
                return
            if sum(combination) == target:
                res.append(combination.copy())
                return
            i = start
            while i < len(candidates):
                combination.append(candidates[i])
                backtack(i + 1, combination)
                combination.pop()
                while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                    i += 1
                i += 1

        backtack(0, [])
        return res
