"""
双指针5
Leetcode 977: https://leetcode.cn/problems/squares-of-a-sorted-array/

因为array中可能有负数，单纯的把每个数平方是不行的。但是单纯平方后的数组一定是两边大中间小。所以两个指针从两头开始，result数组从大往小加。
"""
from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    result = [0] * len(nums)
    index = len(nums) - 1
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] * nums[left] > nums[right] * nums[right]:
            result[index] = nums[left] * nums[left]
            left += 1
        else:
            result[index] = nums[right] * nums[right]
            right -= 1
        index -= 1
    return result


if __name__ == "__main__":
    print(sortedSquares([-4, -1, 0, 3, 10]))
