"""
LeetCode 78: https://leetcode.cn/problems/subsets/description/
这道题唯一的难点是，之前写的都是收集叶子节点的值，这题是收集沿路所有节点的值
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, combination):
            res.append(combination.copy())
            if start >= len(nums):
                return
            for i in range(start, len(nums)):
                combination.append(nums[i])
                backtrack(i + 1, combination)
                combination.pop()

        backtrack(0, [])
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    print(solution.subsets(nums))
