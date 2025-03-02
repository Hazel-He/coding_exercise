"""
LeetCode 131: https://leetcode.cn/problems/palindrome-partitioning/description/
有几个点要注意的：
1. 题目条件是every substring of the partition is a palindrome。所以当s1不是回文串时，就不用backtrack了
2. 为了判断s1是否是回文串，可以用s1 == s1[::-1]，也可以用双指针
3. range要len(s) + 1，是因为当length == 1的时候range(1, 1)不会进入循环
"""
from typing import List


class Solution:
    def isPalindorme(self, s):
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(s, combination):
            if len(s) == 0:
                res.append(combination.copy())
                return

            for i in range(1, len(s) + 1):
                s1 = s[:i]
                s2 = s[i:]
                if self.isPalindorme(s1):
                    combination.append(s1)
                    backtrack(s2, combination)
                    combination.pop()

        backtrack(s, [])
        return res
