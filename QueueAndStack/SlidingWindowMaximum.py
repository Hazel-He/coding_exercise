"""
LeetCode 239: https://leetcode.cn/problems/sliding-window-maximum/description/

这题的重点主要是要维护一个单调递减的deque，这样每次窗口移动的时候，我们只需要看deque的第一个元素就可以了。
但是这个deque不需要存所有的元素，比如2，1，4，2，3，2， k=3
在第一个窗口214的时候，deque里面只需要存4，因为4比2和1都大，所以2和1不可能是最大值，所以存到4的时候，把前面比4的数都pop掉
在第二个窗口142的时候，deque里面一开始只有4，要把2也加进去，因为随着向右移动，2可能会成为最大值，所以要保留
在第三个窗口423的时候，deque里面一开始只有4和2，要把3加进去，因为3比2大，所以2不可能是最大值，所以要pop掉2，此时deque里面只有4和3
在第四个窗口232的时候，deque里面一开始只有4和3，首先要把2加进去，理由同第二个窗口，然后因为4不在窗口里面了，所以要pop掉4（条件为nums[i - k] == q[0]），此时deque里面只有3和2
"""
from collections import deque
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    q = deque()
    res = []
    for i, val in enumerate(nums):
        # while loop保证deque的单调递减,pop掉队列比val小的元素，见窗口一三
        while len(q) != 0 and val > q[-1]:
            q.pop()
        q.append(val)
        # pop掉队列中不在窗口内的元素，见窗口四
        if i >= k and nums[i - k] == q[0]:
            q.popleft()
        if i >= k - 1:
            res.append(q[0])

    return res


if __name__ == '__main__':
    print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]
    print(maxSlidingWindow([1], 1))  # [1]
    print(maxSlidingWindow([1, -1], 1))  # [1, -1]
    print(maxSlidingWindow([7, 2, 4], 2))  # [7, 4]
    print(maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))  # [3, 3, 2, 5]
