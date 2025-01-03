"""
LeetCode 1: https://leetcode.cn/problems/two-sum/
"""
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    num_index = {}
    for i in range(len(nums)):
        expect = target - nums[i]
        if num_index.get(expect) is not None:
            return [num_index.get(expect), i]
        else:
            num_index[nums[i]] = i


if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))
    print(twoSum([3, 2, 4], 6))
    print(twoSum([3, 3], 6))
