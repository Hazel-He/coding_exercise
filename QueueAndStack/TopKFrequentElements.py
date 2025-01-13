"""
LeetCode 347: https://leetcode.cn/problems/top-k-frequent-elements/description/
这题主要难点是top K/bottom K，这类问题可以用heap来解决，heap可以用来维护前K个最大/最小值
Java中heap主要是以priority queue来实现，通过override comparator来实现max heap和min heap
Python有三种形式实现heap，https://builtin.com/data-science/priority-queues-in-python
通常使用heapq或者是PriorityQueue，PriorityQueue是线程安全的，而heapq通常会更快，算法题中通常使用heapq
heapq默认是min heap，如果要实现max heap，需要把元素取负数
https://docs.python.org/3/library/heapq.html
https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python
"""
import heapq
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    # first get the frequency
    num_freq = {}
    for num in nums:
        num_freq[num] = num_freq.get(num, 0) + 1

    # push the frequency value into min heap
    min_heap = []
    for num, freq in num_freq.items():
        heapq.heappush(min_heap, (freq, num))
        # keep the size of min heap to be k
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # get the top k frequent elements. Since it is min heap, the smallest element will be at the top
    # we need to reverse the result
    res = [0] * k
    for i in reversed(range(k)):
        res[i] = heapq.heappop(min_heap)[1]
    return res


if __name__ == '__main__':
    print(topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
    print(topKFrequent([1], 1))  # [1]