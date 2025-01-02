"""
LeetCode 349: https://leetcode.cn/problems/intersection-of-two-arrays/description/

上一题ValidAnagram中使用了数组
那有同学可能问了，遇到哈希问题我直接都用set不就得了，用什么数组啊。
直接使用set 不仅占用空间比数组大，而且速度要比数组慢，set把数值映射到key上都要做hash计算的。
不要小瞧 这个耗时，在数据量大的情况，差距是很明显的。
"""
from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    s = set()
    res = set()
    for num in nums1:
        s.add(num)

    for num in nums2:
        if num in s:
            res.add(num)  # if use list for res, the number may be added multiple times

    return list(res)


if __name__ == "__main__":
    print(intersection([1, 2, 2, 1], [2, 2]))
    print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
    print(intersection([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
    print(intersection([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
    print(intersection([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
    print(intersection([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
