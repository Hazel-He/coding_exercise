"""
LeetCode 383: https://leetcode.cn/problems/ransom-note/description/
"""


def canConstruct(ransomNote: str, magazine: str) -> bool:
    char_count = {}
    for char in magazine:
        char_count[char] = char_count.get(char, 0) + 1

    for char in ransomNote:
        if char_count.get(char) is None:
            return False
        else:
            char_count[char] -= 1
            if char_count[char] == 0:
                char_count.pop(char)

    return True


if __name__ == "__main__":
    print(canConstruct("a", "b"))
    print(canConstruct("aa", "ab"))
    print(canConstruct("aa", "aab"))

