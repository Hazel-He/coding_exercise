"""
LeetCode 344: https://leetcode.cn/problems/reverse-string/description/
"""
from typing import List


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    start = 0
    end = len(s) - 1
    while start < end:
        tmp = s[start]
        s[start] = s[end]
        s[end] = tmp
        start += 1
        end -= 1


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    reverseString(s)
    print(s)
    s = ["H", "a", "n", "n", "a", "h"]
    reverseString(s)
    print(s)