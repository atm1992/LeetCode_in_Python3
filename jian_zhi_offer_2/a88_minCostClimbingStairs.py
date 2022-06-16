# -*- coding: UTF-8 -*-
"""
title: 爬楼梯的最少成本
数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。
每当爬上一个阶梯都要花费对应的体力值，一旦支付了相应的体力值，就可以选择向上爬一个阶梯或者爬两个阶梯。
请找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。


示例 1：
输入：cost = [10, 15, 20]
输出：15
解释：最低花费是从 cost[1] 开始，然后走两步即可到阶梯顶，一共花费 15 。

示例 2：
输入：cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出：6
解释：最低花费方式是从 cost[0] 开始，逐个经过那些 1 ，跳过 cost[3] ，一共花费 6 。


提示：
2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        动态规划。
        dp[i] 表示到达第 i 个阶梯所需的最低花费，dp[i] 可以从dp[i-1]、dp[i-2]转移而来，
        状态转移方程为：dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        边界条件：dp[0] = dp[1] = 0
        由于dp[i]仅与 dp[i-1]、dp[i-2] 有关，所以可使用滚动数组的思想，将空间复杂度优化到 O(1)
        """
        pre_1 = pre_2 = 0
        for i in range(2, len(cost) + 1):
            pre_1, pre_2 = min(pre_1 + cost[i - 1], pre_2 + cost[i - 2]), pre_1
        return pre_1


if __name__ == '__main__':
    print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
