# -*- coding: UTF-8 -*-
"""
title: 跳跃游戏 II
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.


Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2


Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 1000
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """贪心算法，反向查找出发位置。
        考虑最后一步跳跃前所在的位置，该位置通过跳跃能够到达最后一个位置，若有多个位置通过跳跃都能到达最后一个位置，
        则贪心地选择距离最后一个位置最远的那个位置，也就是对应下标最小的那个位置"""
        # 初始时要到达的位置
        position = len(nums) - 1
        steps = 0
        # 跳出循环时，position == 0
        while position > 0:
            # i 取值0~position-1。如果i取值position，则从位置i只需跳0步就可到达position
            for i in range(position):
                if i + nums[i] >= position:
                    # 下一次要到达的位置
                    position = i
                    steps += 1
                    break
        return steps

    def jump_2(self, nums: List[int]) -> int:
        """贪心算法，正向查找可到达的最大位置"""
        # max_pos 表示此次能跳到的最远位置；end 表示上次能跳到的最远位置，也是当前这次跳跃能选择到的最大起始位置；
        # cur 表示当前所在的位置；steps 表示所需的步数
        max_pos = end = cur = steps = 0
        n = len(nums)
        # 当end >= n-1时，跳出while循环。end >= n-1 表示此次跳跃可以到达最后一个位置(n-1)，无需再进入下一次跳跃
        while end < n - 1:
            # 记录当前位置cur能跳到的最远位置
            max_pos = max(max_pos, cur + nums[cur])
            # 若当前位置cur到达了上次能跳到的最远位置，则进入下一次跳跃
            if cur == end:
                end = max_pos
                steps += 1
            cur += 1
        return steps


if __name__ == '__main__':
    print(Solution().jump_2([2, 3, 0, 1, 4]))
