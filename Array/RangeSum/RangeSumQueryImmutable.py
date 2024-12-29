"""
Leetcode 303: https://leetcode.cn/problems/range-sum-query-immutable/description/

Use prefix sum to store the sum of the first i elements in the array. Then the sum of elements from index i to j is
just the sum of the first j elements minus the sum of the first i-1 elements.

"""
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.p_sums = [0] * (len(nums))  # Initialize prefix sums list
        for i in range(len(nums)):
            if i == 0:
                self.p_sums[0] = nums[0]
            else:
                self.p_sums[i] = self.p_sums[i - 1] + nums[i]  # Compute prefix sums incrementally

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.p_sums[right]
        else:
            return self.p_sums[right] - self.p_sums[left - 1]


if __name__ == "__main__":
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    print(obj.sumRange(0, 2))
    print(obj.sumRange(2, 5))
    print(obj.sumRange(0, 5))
