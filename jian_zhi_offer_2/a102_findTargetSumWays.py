# -*- coding: UTF-8 -*-
"""
title: 加减的目标值
给定一个正整数数组 nums 和一个整数 target 。
向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
    例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。


示例 1：
输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

示例 2：
输入：nums = [1], target = 1
输出：1


提示：
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""
from functools import lru_cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """回溯 + 记忆化"""

        @lru_cache(maxsize=None)
        def backtrack(idx: int = 0, target: int = target) -> int:
            if idx == n:
                return 1 if target == 0 else 0
            return backtrack(idx + 1, target - nums[idx]) + backtrack(idx + 1, target + nums[idx])

        n = len(nums)
        return backtrack()

    def findTargetSumWays_2(self, nums: List[int], target: int) -> int:
        """
        动态规划。可将原问题转化为0-1背包方案数问题
        假设nums数组的累加和为total，然后在nums数组中选取一些数，使其变为负数(前面加个负号)，假设这些数(加负号之前的原始值)的累加和为neg，
        假设 这些数加上负号之后，nums数组的累加和恰好为target，即 total - 2 * neg == target，即 neg = (total - target) / 2
        原问题可转化为在nums数组中选取一些数，这些数的累加和为neg
        这个问题可使用动态规划求解，dp[i][j] 表示在nums数组中的前i个元素中选取若干个元素(可以一个都不选)，使得被选中元素的累加和为j，满足这种条件的选取方案数。
        根据nums[i] 与 j 之间的大小关系，可分为两种情况：
        1、j >= nums[i]时，元素i可以被选中，也可以不被选中，此时 dp[i][j] = dp[i-1][j-nums[i]] + dp[i-1][j]
        2、j < nums[i]时，元素i不允许被选中，此时 dp[i][j] = dp[i-1][j]
        根据上面的状态转移方程可知，dp[i] 仅与 dp[i-1] 有关，因此可利用滚动数组的思想来优化空间复杂度。
        边界条件：dp[0][j] 除了dp[0][0] = 1以外，其余均为0。dp[0] 表示没有任何元素可供选取，因此累加和只能为0。
        """
        total = sum(nums)
        # 所有元素相加都达不到target，因为0 <= nums[i]，若再选取部分元素取负号，则只会让total更小
        # 注意：total == target 时，可能不止一种方案，因为元素可以等于0，+0 与 -0 是两种不同的方案
        if total < target:
            return 0
        # 不能被2整除
        if (total - target) & 1:
            return 0
        neg = (total - target) >> 1
        # 初始化二维dp数组中的dp[0]，然后大循环len(nums)次，dp[0] ——> dp[1] ——> …… ——> dp[n]，最终结果为 dp[n][neg]
        dp = [1] + [0] * neg
        for num in nums:
            # j 必须是从neg逆序遍历，因为0 <= nums[i]，所以 j - nums[i] <= j，如果是从0遍历到neg，则更新dp[i][j]时，dp[i-1][j-nums[i]] 已经被更新成了 dp[i][j-nums[i]]
            # 因为j < nums[i]时，dp[i][j] = dp[i-1][j]，所以只需从neg逆序遍历到num即可
            for j in range(neg, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[-1]
