"""
LeetCode 491: https://leetcode.cn/problems/non-decreasing-subsequences/description/
而本题求自增子序列，是不能对原数组进行排序的，排完序的数组都是自增子序列了。
所以不能使用之前的去重逻辑！
同一父节点下的同层上使用过的元素就不能再使用了
"""

from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            if len(path) >= 2:
                res.append(path.copy())

            i = start
            while i < len(nums):
                # 第一个条件是为了保证path是递增的，第二个条件是为了保证nums[i]不重复（去重）
                if (len(path) > 0 and nums[i] < path[-1]) or nums[i] in nums[start:i]:
                    i += 1
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
                i += 1

        backtrack(0, [])
        return res


if __name__ == '__main__':
    nums = [94, 23, 72, 89, -12, 45, 98, 40, 90, -68, 98, 3, 91, 68, 36]
    solution = Solution()
    print(solution.findSubsequences(nums))
