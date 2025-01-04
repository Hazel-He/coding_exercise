"""
LeetCode 438: https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/
"""

from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    # deal with edge case
    if len(p) > len(s):
        return []

    res = []
    array_p = [0] * 26
    for char in p:
        array_p[ord(char) - ord('a')] += 1

    array_s = [0] * 26
    start = end = 0
    # 注意这里的边界条件，要保证loop结束后end指向的是len(p)的最后一个字符
    # 这样才能保证下面的while loop是连贯的
    while end < len(p) - 1:
        array_s[ord(s[end]) - ord('a')] += 1
        end += 1

    while end < len(s):
        # 先把end指向的字符加入array_s，才能保证上一个while loop和这个while loop是连贯的
        array_s[ord(s[end]) - ord('a')] += 1
        # 进行判断
        if array_s == array_p:
            res.append(start)

        array_s[ord(s[start]) - ord('a')] -= 1
        start += 1
        end += 1

    return res


if __name__ == "__main__":
    # print(findAnagrams("cbaebabacd", "abc"))
    print(findAnagrams("abab", "ab"))
