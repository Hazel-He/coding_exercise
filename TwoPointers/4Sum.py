"""
LeetCode 18: https://leetcode.cn/problems/4sum/description/

跟3sum类似，只是多了一层循环，时间复杂度为O(n^3)
"""

from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    # 先判断特殊情况
    if len(nums) < 4:
        return []

    nums.sort()
    # 这里无法像3sum那样剪枝，因为4sum的目标值是变化的
    res = []

    for idx1 in range(0, len(nums) - 3):
        # 去重，如果当前数和上一个数相同，那么跳过
        if idx1 > 0 and nums[idx1] == nums[idx1 - 1]:
            continue
        # idx2从idx1+1开始，不是从1开始
        for idx2 in range(idx1 + 1, len(nums) - 2):
            # 注意这里的去重判别条件是idx2 > idx1 + 1（至少走过一个loop），不是idx2 > 1（因为从idx1+1开始）
            if idx2 > idx1 + 1 and nums[idx2] == nums[idx2 - 1]:
                continue
            # 从这里开始的代码和3sum一样
            left = idx2 + 1
            right = len(nums) - 1
            while left < right:
                if nums[idx1] + nums[idx2] + nums[left] + nums[right] < target:
                    left += 1
                elif nums[idx1] + nums[idx2] + nums[left] + nums[right] > target:
                    right -= 1
                else:
                    res.append([nums[idx1], nums[idx2], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

    return res


if __name__ == "__main__":
    print(fourSum([1, 0, -1, 0, -2, 2], 0))
    print(fourSum([2, 2, 2, 2, 2], 8))
    print(fourSum([-2, -1, -1, 1, 1, 2, 2], 0))
