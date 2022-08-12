# -*- coding: UTF-8 -*-
"""
title: 跳跃游戏
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.


Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:
1 <= nums.length <= 3 * 10^4
0 <= nums[i] <= 10^5
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """贪心算法。依次遍历数组中的每一个位置，并实时维护最远可以到达的位置。在遍历的过程中，若最远可以到达的位置大于等于数组中的最后一个位置，
        则说明最后一个位置可达，因此返回True；若在遍历结束后，最后一个位置仍然不可达，则返回False。"""
        n = len(nums)
        right_most = 0
        for i in range(n):
            if i <= right_most:
                right_most = max(right_most, i + nums[i])
                if right_most >= n - 1:
                    return True
            else:
                return False


if __name__ == '__main__':
    print(Solution().canJump([3, 0, 8, 2, 0, 0, 1]))
