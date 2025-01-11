"""
LeetCode 225: https://leetcode.cn/problems/implement-stack-using-queues/description/
"""


class MyStack:

    def __init__(self):
        self.lst = []
        self.size = 0

    def push(self, x: int) -> None:
        self.lst.append(x)
        self.size += 1

    def pop(self) -> int:
        for i in range(self.size - 1):
            self.lst.append(self.lst.pop(0))
        self.size -= 1
        return self.lst.pop(0)

    def top(self) -> int:
        res = self.lst.pop()
        self.lst.append(res)
        return res

    def empty(self) -> bool:
        return self.size == 0