"""
LeetCode 454: https://leetcode.cn/problems/4sum-ii/description/
"""

from typing import List


def fourSumCount(nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    num12_count = {}
    res = 0
    for num1 in nums1:
        for num2 in nums2:
            num12_sum = num1 + num2
            num12_count[num12_sum] = num12_count.get(num12_sum, 0) + 1

    for num3 in nums3:
        for num4 in nums4:
            num34_sum = num3 + num4
            expect = 0 - num34_sum
            if num12_count.get(expect) is not None:
                res += num12_count.get(expect)

    return res


if __name__ == "__main__":
    fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2])
    fourSumCount([0], [0], [0], [0])
