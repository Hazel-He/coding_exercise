"""
最基本的二分搜索
Leetcode 704: https://leetcode.cn/problems/binary-search/

给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1

注意事项：
1. python中整除是"//"， java是"/"
2. 算mid不要用 "(left+right)//2" 会overflow，要用left + (right-left)//2
3. 边界条件（什么时候要等于），取决于定义的数据开闭合
   1）[] -> [1,1]
   2) [) -> [1,1]就不行，必须要[1,2)
   3) (] -> (1,2]
"""
from typing import List


# 第一种：[left, right]
def search1(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1  # left, right 两边选取的时候都包含
    while left <= right:  # 两边都包含的话可以等于
        mid = left + (right - left) // 2
        if target > nums[mid]:
            left = mid + 1  # 因为两边都要包含，所以+1而不是=mid
        elif target < nums[mid]:
            right = mid - 1  # 因为两边都要包含，所以-1而不是=mid
        else:
            return mid
    return -1


# 第二种：[left, right)
def search2(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)  # 包含left所以left等于0，不包含right所以right直接等于len
    while left < right:  # 因为不包含right，这里是小于
        mid = left + (right - left) // 2
        if target > nums[mid]:
            left = mid + 1  # 包含left，left得加一，因为此时mid不符合条件，不能包括mid
        elif target < nums[mid]:
            right = mid  # 不包含right，right直接等于mid，因为此时mid不符合条件，不能包括mid
        else:
            return mid
    return -1


if __name__ == "__main__":
    print(search1([-1, 0, 3, 5, 9, 12], 9))  # return 4
    print(search1([-1, 0, 3, 5, 9, 12], 2))  # return -1
    print(search2([-1, 0, 3, 5, 9, 12], 9))  # return 4
    print(search2([-1, 0, 3, 5, 9, 12], 2))  # return -1
