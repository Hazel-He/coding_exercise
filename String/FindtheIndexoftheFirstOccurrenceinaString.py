"""
LeetCode 28: https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
next array跟strStr的计算逻辑本质是一样的。
i都是长的字符串，不会回退
j都是匹配值，会回退，回退的位置都是next_array[j-1]
相等的时候，两个都加
不相等的时候，j回退，直到相等或者j=0
"""
from typing import List


def buildNextArray(needle: str) -> List[int]:
    next_array = [0] * len(needle)
    j, i = 0, 1
    while i < len(needle):
        if needle[i] == needle[j]:
            next_array[i] = j + 1
            i += 1
            j += 1
        else: # 不相等的情况
            if j == 0: # j如果是0，无法回退，next——array赋值0
                next_array[i] = 0
                i += 1
            else: # j不是0，回退
                j = next_array[j-1]
    return next_array


def strStr(haystack: str, needle: str) -> int:
    next_array = buildNextArray(needle)
    i, j = 0, 0
    while i < len(haystack):
        if haystack[i] == needle[j]:
            if j == len(needle) - 1:
                return i - len(needle) + 1
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = next_array[j - 1]
    return -1




if __name__ == "__main__":
    print(buildNextArray("aabb"))


