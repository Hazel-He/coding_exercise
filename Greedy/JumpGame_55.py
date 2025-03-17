"""
LeetCode 55: https://leetcode.cn/problems/jump-game/description/
刚看到本题一开始可能想：当前位置元素如果是 3，我究竟是跳一步呢，还是两步呢，还是三步呢，究竟跳几步才是最优呢？
其实跳几步无所谓，关键在于可跳的覆盖范围！
不一定非要明确一次究竟跳几步，每次取最大的跳跃步数，这个就是可以跳跃的覆盖范围。
这个范围内，别管是怎么跳的，反正一定可以跳过来。
那么这个问题就转化为跳跃覆盖范围究竟可不可以覆盖到终点！
每次移动取最大跳跃步数（得到最大的覆盖范围），每移动一个单位，就更新最大覆盖范围。
贪心算法局部最优解：每次取最大跳跃步数（取最大覆盖范围），整体最优解：最后得到整体最大覆盖范围，看是否能到终点。
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        i = 0
        while i < len(nums) and i <= cover:
            cover = max(cover, i + nums[i])
            if cover >= len(nums) - 1:
                return True
            i += 1
        return False