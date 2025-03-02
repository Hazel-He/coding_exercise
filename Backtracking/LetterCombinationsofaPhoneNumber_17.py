"""
LeetCode 17: https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        result = []
        digits_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        groups = []
        for s in digits:
            groups.append(digits_letters[s])

        def backtrack(index, combination):
            if index == len(digits):
                result.append("".join(combination))
                return

            for char in groups[index]:
                combination.append(char)
                backtrack(index + 1, combination)
                combination.pop()

        backtrack(0, [])
        return result
