"""
LeetCode 459: https://leetcode.cn/problems/repeated-substring-pattern/description/
"""


def repeatedSubstringPattern(s: str) -> bool:
    # 如果存在子串s'，那么s的长度一定是s'的n倍，并且s'一定是s的前缀
    for i in range(len(s) // 2):
        if len(s) % (i + 1) == 0:
            subString = s[0:i + 1]
            subStringLen = i + 1
            match = True
            for j in range(i + 1, len(s)):
                if s[j] != subString[j % subStringLen]:
                    match = False
                    break
            if match:
                return True

    return False


if __name__ == '__main__':
    print(repeatedSubstringPattern("aabaaba"))
