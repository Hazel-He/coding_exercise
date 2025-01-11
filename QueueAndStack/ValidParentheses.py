"""
LeetCode 20: https://leetcode.cn/problems/valid-parentheses/description/
"""


def isValid(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    match_list = []
    for char in s:
        if char == "(":
            match_list.append(")")
        elif char == "[":
            match_list.append("]")
        elif char == "{":
            match_list.append("}")
        elif len(match_list) == 0:
            return False
        else:
            val = match_list.pop()
            if val != char:
                return False

    if len(match_list) != 0:
        return False

    return True


if __name__ == '__main__':
    print(isValid("()"))  # True
    print(isValid("()[]{}"))  # True
    print(isValid("(]"))  # False