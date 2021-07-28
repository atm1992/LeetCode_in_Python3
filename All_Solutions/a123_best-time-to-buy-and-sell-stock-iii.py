# -*- coding: UTF-8 -*-
"""
title：买卖股票的最佳时机 III
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Example 4:
Input: prices = [1]
Output: 0
 

Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^5
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        # 定义第一天的状态
        dp_i10 = 0
        dp_i20 = 0
        dp_i11 = -prices[0]
        dp_i21 = -prices[0]
        for price in prices[1:]:
            dp_i10 = max(dp_i10, dp_i11 + price)
            # 因为对于任意一天的dp[x][0][0]，值都是0
            dp_i11 = max(dp_i11, -price)
            dp_i20 = max(dp_i20, dp_i21 + price)
            dp_i21 = max(dp_i21, dp_i10 - price)
        # 最后一天，有2次交易，并且没有持股。此时的利润为最终利润
        return dp_i20
