"""
二分搜索变式
Leetcode 35: https://leetcode.cn/problems/search-insert-position/
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

示例 1:
输入: nums = [1,3,5,6], target = 5
输出: 2

示例 2:
输入: nums = [1,3,5,6], target = 2
输出: 1

示例 3:
输入: nums = [1,3,5,6], target = 7
输出: 4
"""
from typing import List


# 采用了[left,right)的解法
def searchInsert(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if target < nums[mid]:
            right = mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid

    return right


# 采用了[left,right]的解法
def searchInsert2(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid

    return right + 1  # 也可以是return left


if __name__ == "__main__":
    print(searchInsert([1, 3, 5, 6], 5))
    print(searchInsert([1, 3, 5, 6], 2))
    print(searchInsert([1, 3, 5, 6], 7))

    print(searchInsert([1, 3, 5, 6], -1))
