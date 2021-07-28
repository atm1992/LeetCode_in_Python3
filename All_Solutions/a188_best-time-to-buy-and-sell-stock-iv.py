# -*- coding: UTF-8 -*-
"""
title：买卖股票的最佳时机 IV
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
Find the maximum profit you can achieve. You may complete at most k transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


Example 1:
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
 

Constraints:
0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
"""
from typing import List


class Solution:
    """
    有效的交易由买入和卖出构成，至少需要两天；反之，当天买入当天卖出则视为一次无效交易。若给定的最大交易次数 k <= n/2，
    则这个 k 可以有效约束交易次数；若给定的 k > n/2 ，则这个 k 实际上起不到约束作用，此时的k等价于正无穷，问题退化为不限交易次数。
    """

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or len(prices) < 2 or k < 1:
            return 0

        def maxProfit_k_inf(prices):
            n = len(prices)
            res = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            return res

        def maxProfit_k_others(prices, k):
            n = len(prices)
            dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
            for i in range(n):
                for j in range(1, k + 1):
                    if i == 0:
                        dp[i][j][0] = 0
                        dp[i][j][1] = -prices[0]
                    else:
                        dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                        dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
            # return dp[n - 1][k][0]
            return dp[-1][-1][0]

        n = len(prices)
        if k > n / 2:
            return maxProfit_k_inf(prices)
        else:
            return maxProfit_k_others(prices, k)
