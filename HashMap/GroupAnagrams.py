"""
LeetCode 49: https://leetcode.cn/problems/group-anagrams/description/
"""

from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    array_list = {}
    for str_ in strs:
        array = [0] * 26
        for char in str_:
            array[ord(char) - ord('a')] += 1
        # list cannot be the key, need to convert to tuple or string
        if array_list.get(tuple(array)) is not None:
            array_list[tuple(array)].append(str_)
        else:
            array_list[tuple(array)] = [str_]

    return list(array_list.values())


if __name__ == "__main__":
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(groupAnagrams([""]))
    print(groupAnagrams(["a"]))