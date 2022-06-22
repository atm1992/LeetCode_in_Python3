# -*- coding: UTF-8 -*-
"""
title: 最少的硬币数目
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
你可以认为每种硬币的数量是无限的。


示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0

示例 4：
输入：coins = [1], amount = 1
输出：1

示例 5：
输入：coins = [1], amount = 2
输出：2


提示：
1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4

解题思路：
不能先排序(降序)，再贪心。例如：coins = [7, 3, 2], amount = 8
"""
from functools import lru_cache
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        自顶向下(从整体到局部)的递归 + 记忆化搜索
        假设F(S)表示组成金额S所需的最小硬币数量，[c0, c1, ……, cn-1] 表示可选的n种硬币面值。
        状态转移方程为：F(S) = F(S - C) + 1，其中的C表示组成金额S所需的最后一枚硬币面值，
        因此，可以枚举c0, c1, ……, cn-1作为最后一枚硬币C，然后从中选择最小值。
        边界条件：F(0) = 0
        """

        @lru_cache(maxsize=None)
        def helper(amount: int) -> int:
            if amount == 0:
                return 0
            elif amount < 0:
                return -1
            # 因为1 <= coins[i], 且 amount <= 10^4，所以 硬币个数 <= 10^4 / 1 = 10000 < 10001
            res = 10001
            # 枚举凑成amount的最后一枚硬币
            for coin in coins:
                tmp = helper(amount - coin)
                # 不能直接在amount小于coin时，break。此时若退出for循环，则返回的res会有问题，
                # 因为在amount逐步减到小于当期coin之前，res可能已经被修改了，而不再是初始值10001，这种情况下，最终返回的不是预期的-1
                # 在amount小于coin时，不应该去修改res
                if tmp >= 0:
                    res = min(res, tmp + 1)
            return -1 if res == 10001 else res

        return helper(amount)

    def coinChange_2(self, coins: List[int], amount: int) -> int:
        """
        自底向上(从局部到整体)的动态规划。优于上面的方法
        """
        # 总金额为0时，所需的最少硬币个数为0
        dp = [0] + [10001] * amount
        # 枚举凑成amount的最后一枚硬币
        for coin in coins:
            # 因为要求 i - coin >= 0，所以从coin开始枚举i
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[-1] == 10001 else dp[-1]
