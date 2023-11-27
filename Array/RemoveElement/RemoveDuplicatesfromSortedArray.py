"""
双指针2
Leetcode 26: https://leetcode.cn/problems/remove-duplicates-from-sorted-array/

因为是有序的，重复一定是相邻的
"""
from typing import List


def removeDuplicates(nums: List[int]) -> int:
    fast = 0
    slow = 0
    while fast < len(nums):
        if nums[fast] != nums[slow]:
            nums[slow + 1] = nums[fast]  # 不等于的时候将fast的值赋予给slow的下一个
            slow += 1
            fast += 1
        else:
            fast += 1
    return slow + 1
