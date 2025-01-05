"""
LeetCode 15: https://leetcode.cn/problems/3sum/description/
有剪枝和去重的操作
时间复杂度：O(n^2):
    数组排序: O(NlogN)
    遍历数组: O(n)
    双指针遍历: O(n)
    总体: O(NlogN)+O(n)∗O(n) -> O(n^2)
空间复杂度：O(1)
"""

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    # deal with edge case
    if len(nums) < 3:
        return []

    nums.sort()
    # 剪枝，如果最小的数都大于0，那么不可能有三个数相加等于0
    if nums[0] > 0:
        return []

    res = []
    for i in range(len(nums) - 2):
        # 去重，如果当前数和上一个数相同，那么跳过
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            # 若和大于0，说明 nums[right]太大，right左移
            if nums[i] + nums[left] + nums[right] > 0:
                right -= 1
            # 若和小于0，说明 nums[left]太小，left右移
            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            # 和等于0，加入结果集，left右移，right左移
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                # 去重，如果左指针指向的数和上一个数相同，那么跳过
                # 不能无限移动，考虑0，0，0，0
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                right -= 1
                # 去重，如果右指针指向的数和上一个数相同，那么跳过
                # 同上
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return res


if __name__ == "__main__":
    print(threeSum([-1, 0, 1, 2, -1, -4]))
    print(threeSum([]))
    print(threeSum([0]))
    print(threeSum([0, 0, 0, 0]))
