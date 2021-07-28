# -*- coding: UTF-8 -*-
"""
title：使用最小花费爬楼梯。
数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。
示例 1:
输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
示例 2:
输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。

注意：
1、cost 的长度将会在 [2, 1000]。
2、每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。

题目理解：可以自由选择将数组中的第一个元素或第二个元素作为起始点，并且每次都可以自由选择是走一步还是走两步，
最后将所有经过的数组元素进行累加，要求和为最小。
解题思路：动态规划
因为能到达i处的只有i-1与i-2处的阶梯，所以 dp[i] = min(dp[i-1],dp[i-2]) + cost[i] ，
dp数组中的元素为到达i处阶梯所需的最小花费。
最终返回结果为 min(dp[n-1],dp[n-2])，因为cost[n]为0
"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        # 题目已告知cost的长度大于等于2，所以无需考虑cost长度小于2的情况。
        # 若cost长度为2，则返回结果直接为min(cost[0], cost[1])，即 min(dp[0], dp[1])
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[n - 1], dp[n - 2])

    def minCostClimbingStairs_2(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [cost[0], cost[1]]
        for i in range(2, n):
            dp[i % 2] = min(dp[-1], dp[-2]) + cost[i]
        return min(dp[-1], dp[-2])

    def minCostClimbingStairs_3(self, cost: List[int]) -> int:
        # 这里直接复用cost数组来代替上面的dp数组，因为dp数组的前两个初始值正好为cost[0], cost[1]
        n = len(cost)
        for i in range(2, n):
            cost[i] = min(cost[i - 1], cost[i - 2]) + cost[i]
        return min(cost[-1], cost[-2])


if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    s = Solution()
    print(s.minCostClimbingStairs(cost))
