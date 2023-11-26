"""
二分搜索变式
Leetcode 34: https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/

给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]
"""
from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    def rightIndex(nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        right_idx = -1
        while left <= right:
            mid = left + (right - left) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                right_idx = mid
                left = mid + 1
        return right_idx

    def leftIndex(nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        left_idx = -1
        while left <= right:
            mid = left + (right - left) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                left_idx = mid
                right = mid - 1
        return left_idx

    right_idx = rightIndex(nums, target)
    left_idx = leftIndex(nums, target)
    return [left_idx, right_idx]


if __name__ == "__main__":
    print(searchRange([5, 7, 7, 8, 8, 10], 8))
    print(searchRange([5, 7, 7, 8, 8, 10], 6))
    print(searchRange([], 0))
