"""
LeetCode 45: https://leetcode.cn/problems/jump-game-ii/description/
但思路是相似的，还是要看最大覆盖范围。
本题要计算最少步数，那么就要想清楚什么时候步数才一定要加一呢？
贪心的思路，局部最优：当前可移动距离尽可能多走，如果还没到终点，步数再加一。整体最优：一步尽可能多走，从而达到最少步数。
思路虽然是这样，但在写代码的时候还不能真的能跳多远就跳多远，那样就不知道下一步最远能跳到哪里了。
所以真正解题的时候，要从当前覆盖范围出发，不管怎么跳，覆盖范围内一定是可以跳到的，然后在当前覆盖范围内，找到能跳的最远的位置，覆盖范围一旦覆盖了终点，得到的就是最少步数！
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # 特殊case，如果只有一个元素，不需要跳跃
        if len(nums) == 1:
            return 0
        steps = 0
        idx = 0
        while idx < len(nums):
            cover = idx + nums[idx] + 1  # 当前覆盖范围
            if cover >= len(nums): # 如果覆盖范围已经覆盖终点，只需要再跳一步
                return steps + 1
            # 如果当前覆盖范围还没覆盖终点，找到覆盖范围内能跳的最远的位置
            # 注意不是找当前覆盖范围的最大值，而是当前覆盖范围的index + nums[index]的最大值 - 这才是覆盖范围内能跳的最远的位置
            maxCover = 0
            for i in range(idx + 1, cover):
                if i + nums[i] > maxCover:
                    maxCover = i + nums[i]
                    idx = i
            steps += 1

        return steps + 1
