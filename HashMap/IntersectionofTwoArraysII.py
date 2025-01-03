"""
LeetCode 350: https://leetcode.cn/problems/intersection-of-two-arrays-ii/description/
"""

from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    num1_count = {}
    res = []
    for num in nums1:
        num1_count[num] = num1_count.get(num, 0) + 1

    for num in nums2:
        if num1_count.get(num) is not None:
            res.append(num)
            num1_count[num] -= 1
            if num1_count[num] == 0:
                num1_count.pop(num)

    return res


if __name__ == "__main__":
    print(intersect([1, 2, 2, 1], [2, 2]))
    print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
