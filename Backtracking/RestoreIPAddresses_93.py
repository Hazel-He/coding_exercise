"""
LeetCode 93: https://leetcode.cn/problems/restore-ip-addresses/description/
跟131很像，通过切割字符串，来组合
有几个剪枝的：
1. 最多切3刀，所以cutSum == 3时，就不用再切了
2. 最多不超过3位，所以树的每层的数量不会超过3 - for i in range(startIndex + 1, startIndex + 4)
"""

from typing import List


class Solution:
    def isValidIPInteger(self, s):
        if len(s) == 0 or len(s) > 3:
            return False
        if len(s) > 1 and s[0] == "0":
            return False
        if 0 <= int(s) <= 255:
            return True
        return False

    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtarck(startIndex, combination, cutSum):
            if cutSum == 3:
                if self.isValidIPInteger(s[startIndex:]):
                    res.append(".".join(combination) + "." + s[startIndex:])
                return
            for i in range(startIndex + 1, startIndex + 4):  # 这里是startIndex + 4，不是startIndex + 3, 因为range是左闭右开
                if self.isValidIPInteger(s[startIndex:i]):
                    combination.append(s[startIndex:i])
                    cutSum += 1
                    backtarck(i, combination, cutSum)
                    combination.pop()
                    cutSum -= 1

        backtarck(0, [], 0)
        return res


if __name__ == '__main__':
    s = "23412314235"
    solution = Solution()
    print(solution.restoreIpAddresses(s))
