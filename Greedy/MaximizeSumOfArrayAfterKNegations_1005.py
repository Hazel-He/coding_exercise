"""
LeetCode 1005: https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/description/
贪心的思路，局部最优：让绝对值大的负数变为正数，当前数值达到最大，整体最优：整个数组和达到最大。
局部最优可以推出全局最优。
那么如果将负数都转变为正数了，K依然大于0，此时的问题是一个有序正整数序列，如何转变K次正负，让数组和达到最大。
那么又是一个贪心：局部最优：只找数值最小的正整数进行反转，当前数值和可以达到最大（例如正整数数组{5, 3, 1}，反转1 得到-1 比 反转5得到的-5 大多了），全局最优：整个数组和达到最大。
我这里其实是为了给大家展现出来 经常被大家忽略的贪心思路，这么一道简单题，就用了两次贪心！
"""
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxNegativeIndex = 0

        # 把所有的负数都转正
        for index, num in enumerate(nums):
            if k <= 0:
                return sum(nums)
            if num >= 0:
                break
            if num < 0 and k > 0:
                nums[index] = -1 * num
                k -= 1
                maxNegativeIndex = index

        # 现在所有数都是正数，转最小的正数
        if k % 2 == 0:
            return sum(nums)
        else:
            if maxNegativeIndex < len(nums) - 1:
                minPositiveIndex = maxNegativeIndex + 1
                if nums[maxNegativeIndex] < nums[minPositiveIndex]:
                    nums[maxNegativeIndex] = nums[maxNegativeIndex] * -1
                else:
                    nums[minPositiveIndex] = -1 * nums[minPositiveIndex]
            else:
                nums[maxNegativeIndex] = nums[maxNegativeIndex] * -1
            return sum(nums)
