# -*- coding: UTF-8 -*-
"""
title: 使用最小花费爬楼梯
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.


Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.


Constraints:
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
