# -*- coding: UTF-8 -*-
"""
title：最佳买卖股票时机含冷冻期
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0
 

Constraints:
1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        n = len(prices)
        # 定义一个二维数组dp
        dp = [[0] * 2 for _ in range(n)]
        # 初始化
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        dp[1][1] = max(dp[0][1], -prices[1])
        for i in range(2, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        return dp[-1][0]
