"""
Leetcode 209: https://leetcode.cn/problems/minimum-size-subarray-sum/
"""
from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    start = 0
    end = 0
    minLen = float('inf')
    total = 0  # 累加值
    while end < len(nums):
        total = total + nums[end]
        if total < target:
            end += 1  # 如果累加值不到target，end继续移动
        else:
            curLen = end - start + 1
            minLen = min(curLen, minLen)
            # 如果累加值大于等于target，开始移动start。注意这里要用while，一直移动start直到小于start。例子target=100，[1,1,1,1,100]
            # 只是if的话，第一个1就会停了
            while start < end and total - nums[start] >= target:
                total = total - nums[start]
                start += 1
                curLen = end - start + 1
                minLen = min(curLen, minLen)
            end += 1
    if minLen == float('inf'):
        return 0
    else:
        return minLen


if __name__ == "__main__":
    print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
