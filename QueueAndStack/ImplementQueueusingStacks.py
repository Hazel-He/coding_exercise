"""
LeetCode 232: https://leetcode.cn/problems/implement-queue-using-stacks/description/
"""


class MyQueue:

    def __init__(self):
        self.stackIn = []
        self.stackOut = []

    def push(self, x: int) -> None:
        self.stackIn.append(x)

    def pop(self) -> int:
        if self.stackOut:
            return self.stackOut.pop(0)
        else:
            while self.stackIn:
                self.stackOut.append(self.stackIn.pop(0))
            return self.stackOut.pop(0)

    def peek(self) -> int:
        res = self.pop()
        self.stackOut.insert(0, res)
        return res

    def empty(self) -> bool:
        return len(self.stackIn) == 0 and len(self.stackOut) == 0
