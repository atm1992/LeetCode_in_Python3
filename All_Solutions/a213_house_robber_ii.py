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
        dp[i] 表示偷窃前i间房屋所能获得的最高金额，状态转移方程：dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        边界条件：dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
        本题与题198的区别在于：第一间房屋和最后一间房屋不能在同一晚上偷窃。因此可分为两种情况，分别进行动态规划，然后取两者的较大值。
        1、计算 0 ~ n-2 的最高金额
        2、计算 1 ~ n-1 的最高金额
        """

        def helper(start: int, end: int) -> int:
            pre_2, pre_1 = nums[start], max(nums[start], nums[start + 1])
            for i in range(start + 2, end + 1):
                pre_2, pre_1 = pre_1, max(pre_2 + nums[i], pre_1)
            return pre_1

        # 1 <= nums.length
        n = len(nums)
        if n < 3:
            return max(nums)
        return max(helper(0, n - 2), helper(1, n - 1))

    def rob_2(self, nums: List[int]) -> int:
        """
        动态规划。
        dp[i] 表示偷窃前i间房屋所能获得的最高金额，状态转移方程：dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        边界条件：dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
        本题与题198的区别在于：第一间房屋和最后一间房屋不能在同一晚上偷窃。因此可分为两种情况，分别进行动态规划，然后取两者的较大值。
        1、计算 0 ~ n-2 的最高金额
        2、计算 1 ~ n-1 的最高金额
        """
        # 1 <= nums.length
        n = len(nums)
        if n < 3:
            return max(nums)
        # 计算 0 ~ n-2 的最高金额
        pre_0_2, pre_0_1 = nums[0], max(nums[0], nums[1])
        # 计算 1 ~ n-1 的最高金额
        pre_1_2, pre_1_1 = 0, nums[1]
        for i in range(2, n):
            if i < n - 1:
                pre_0_2, pre_0_1 = pre_0_1, max(pre_0_2 + nums[i], pre_0_1)
            pre_1_2, pre_1_1 = pre_1_1, max(pre_1_2 + nums[i], pre_1_1)
        return max(pre_0_1, pre_1_1)


if __name__ == '__main__':
    print(Solution().rob(nums=[1, 2, 3, 1]))
