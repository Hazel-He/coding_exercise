'''
LeetCode 904: https://leetcode.cn/problems/fruit-into-baskets/description/
'''

from typing import List


def totalFruit(fruits: List[int]) -> int:
    result = 0
    tmp_result = 0
    bucket = dict()
    start = 0
    end = 0
    while end < len(fruits):
        if fruits[end] not in bucket and len(bucket) == 2:
            value = bucket[fruits[start]] - 1
            if value == 0:
                bucket.pop(fruits[start])
            else:
                bucket[fruits[start]] = value
            tmp_result -= 1
            start += 1
        else:
            if fruits[end] in bucket:
                bucket[fruits[end]] += 1
            else:
                bucket[fruits[end]] = 1
            tmp_result += 1
            result = max(result, tmp_result)
            end += 1
    return result


if __name__ == "__main__":
    print(totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
