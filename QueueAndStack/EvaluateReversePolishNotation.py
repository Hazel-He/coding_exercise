"""
LeetCode 150: https://leetcode.cn/problems/evaluate-reverse-polish-notation/description/
"""
from typing import List


def evalRPN(tokens: List[str]) -> int:
    stack = []
    for token in tokens:
        if token == "+" or token == "-" or token == "*" or token == "/":
            # Notice that The division between two integers always truncates toward zero.
            # replace to // will be different when doing negative number
            # so use int() to do that
            num1 = stack.pop()
            num2 = stack.pop()
            res = eval(str(num2) + token + str(num1))
            stack.append(int(res))
        else:
            stack.append(int(token))

    return stack.pop()


if __name__ == '__main__':
    print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
