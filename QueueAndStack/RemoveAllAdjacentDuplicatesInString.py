"""
LeetCode 1047: https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/description/
"""


def removeDuplicates(s: str) -> str:
    stack = []
    for char in s:
        if len(stack) == 0:
            stack.append(char)
        else:
            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

    return "".join(stack)


if __name__ == '__main__':
    print(removeDuplicates("abbaca"))  # ca
    print(removeDuplicates("azxxzy"))  # ay
    print(removeDuplicates("a"))  # a
    print(removeDuplicates("aa"))  # ""
    print(removeDuplicates("baab"))  # ""
