# -*- coding: UTF-8 -*-
"""
title: 打家劫舍 II
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3


Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        动态规划。
        dp[i] 表示前 i 间房屋能偷窃到的最高总金额。状态转移方程为：dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        边界条件：
        dp[0] = nums[0]                         # 只有一间房
        dp[1] = max(nums[0], nums[1])           # 只有两间房
        本题与题198的区别在于：第一间房屋和最后一间房屋不能在同一晚上偷窃。因此可分为两种情况，分别进行动态规划，然后取两者的较大值。
        1、计算 0 ~ n-2 的最高总金额
        2、计算 1 ~ n-1 的最高总金额
        """

        def dfs(nums: List[int], start: int, end: int) -> int:
            first = nums[start]
            second = max(nums[start], nums[start + 1])
            for i in range(start + 2, end + 1):
                first, second = second, max(first + nums[i], second)
            return second

        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)
        else:
            return max(dfs(nums, 0, n - 2), dfs(nums, 1, n - 1))


if __name__ == '__main__':
    print(Solution().rob(nums=[1, 2, 3, 1]))
