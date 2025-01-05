"""
LeetCode 541: https://leetcode.cn/problems/reverse-string-ii/description/
"""
from typing import List


def reverseStr(s: str, k: int) -> str:
    def reverse(s: List[str]):
        start = 0
        end = len(s) - 1
        while start < end:
            tmp = s[start]
            s[start] = s[end]
            s[end] = tmp
            start += 1
            end -= 1
        return s

    s = list(s)
    for i in range(0, len(s), 2 * k):
        # replace substring 可以避免index out of bound的问题
        # ['a', 'b', 'c'][0:10] = ['a', 'b', 'c']
        # 不然要考虑边界条件
        s[i:i+k] = reverse(s[i:i+k])

    return "".join(s)


if __name__ == "__main__":
    print(reverseStr("abcdefg", 2))
    print(reverseStr("abcd", 2))
    print(reverseStr("a", 2))
