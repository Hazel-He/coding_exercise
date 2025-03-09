"""
LeetCode 455: https://leetcode.cn/problems/assign-cookies/description/
"""

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        i = 0

        for cookie in s:
            if i < len(g) and cookie >= g[i]:
                res += 1
                i += 1

        return res