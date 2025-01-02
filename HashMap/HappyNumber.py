"""
Leetcode 202: https://leetcode.cn/problems/happy-number/description/

The key is "loops endlessly in a cycle", which means the sum should be appeared again.
"""


def isHappy(n: int) -> bool:
    def getSum(n):
        res = 0
        while n:
            res += (n % 10) ** 2
            n = n // 10
        return res

    pre_sum = set()
    while True:
        sum_ = getSum(n)
        if sum_ == 1:
            return True
        if sum_ in pre_sum:
            return False
        else:
            pre_sum.add(sum_)
            n = sum_


if __name__ == "__main__":
    print(isHappy(19))
    print(isHappy(2))
