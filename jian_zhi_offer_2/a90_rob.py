# -*- coding: UTF-8 -*-
"""
title: 环形房屋偷盗
一个专业的小偷，计划偷窃一个环形街道上沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组 nums ，请计算 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。


示例 1：
输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

示例 2：
输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 3：
输入：nums = [0]
输出：0


提示：
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
        本题与上一题的区别在于：第一间房屋和最后一间房屋不能在同一晚上偷窃。因此可分为两种情况，分别进行动态规划，然后取两者的较大值。
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
        本题与上一题的区别在于：第一间房屋和最后一间房屋不能在同一晚上偷窃。因此可分为两种情况，分别进行动态规划，然后取两者的较大值。
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
    print(Solution().rob([1, 2, 3, 1]))
