# -*- coding: UTF-8 -*-
"""
title: 打家劫舍
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.


Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """回溯。会超时"""
        n = len(nums)
        res = 0

        def dfs(idx: int = 0, path: list = []) -> None:
            nonlocal res
            if idx >= n:
                res = max(res, sum(path))
            for i in range(idx, n):
                path.append(nums[i])
                dfs(i + 2)
                path.pop()

        dfs()
        return res

    def rob_2(self, nums: List[int]) -> int:
        """
        动态规划。
        dp[i] 表示前 i 间房屋能偷窃到的最高总金额。状态转移方程为：dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        边界条件：
        dp[0] = nums[0]      # 只有一间房
        dp[1] = max(nums[0], nums[1])           # 只有两间房
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[n - 1]

    def rob_3(self, nums: List[int]) -> int:
        """
        动态规划。使用滚动数组降低空间复杂度
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)
        dp = [nums[0], max(nums[:2])]
        for i in range(2, n):
            dp[i % 2] = max(dp[(i - 2) % 2] + nums[i], dp[(i - 1) % 2])
        return dp[(n - 1) % 2]


if __name__ == '__main__':
    print(Solution().rob_2([2, 7, 9, 3, 1]))
