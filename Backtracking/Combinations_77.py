"""
LeetCode 77: https://leetcode.cn/problems/combinations/description/
首先是关于回溯法点：
1. 回溯主要利用递归来实现多层for loop的做法，比如此题如果k=50，那么就需要50层for loop，这是不现实的，所以用递归来实现。
2. 回溯的本质是暴力解法，唯一能优化的就是剪枝处理。比如此题，当剩余的数字+已经选中的数字的长度小于k时，就不用再继续loop了，所以终止的end不需要是n

还有一些python需要注意的点：
1. 在收集结果的时候，需要用combination.copy()，否则会收集到空数组，因为combination是引用，会被后续的pop操作改变
2. range的范围，要注意n - (k - len(combination)) + 2，这个是剪枝的关键
3. +2是因为range的范围是左闭右开，所以要+1。如果是左闭右闭，就是+1
4. 因为backtracking是inner函数，所以result，n，k都是共享的，不需要传参
"""

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(start, combination):
            if len(combination) == k:
                result.append(combination.copy())
                return
            for i in range(start, n - (k - len(combination)) + 2):
                combination.append(i)
                backtracking(i + 1, combination)
                combination.pop()

        result = []
        backtracking(1, [])
        return result
