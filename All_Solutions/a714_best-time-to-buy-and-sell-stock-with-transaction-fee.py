# -*- coding: UTF-8 -*-
"""
title：买卖股票的最佳时机含手续费
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.
Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


Example 1:
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Example 2:
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
 

Constraints:
1 <= prices.length <= 5 * 10^4
1 <= prices[i] < 5 * 10^4
0 <= fee < 5 * 10^4
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        动态规划
        dp[i][0] 表示第 i 天交易完后手里没有股票的最大利润；dp[i][1] 表示第 i 天交易完后手里持有一支股票的最大利润(i从0开始)。
        dp[i][0] 的状态转移方程：dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
        dp[i][1] 的状态转移方程：dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        初始值：
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        由状态转移方程可知，dp[i] 仅与 dp[i-1]有关，所以可使用滚动数组的思想来降低空间复杂度
        """
        # sell -- dp[*][0]；buy -- dp[*][1]
        sell, buy = 0, -prices[0]
        for price in prices[1:]:
            sell, buy = max(sell, buy + price - fee), max(buy, sell - price)
        return sell

    def maxProfit_2(self, prices: List[int], fee: int) -> int:
        """贪心。将手续费fee算进买入股票时的花费(buy = prices[i] + fee)"""
        buy = prices[0] + fee
        res = 0
        # 通过下面这两种操作，可以总是在极小值点买入，然后在极大值点卖出，从而获得最大的利润。
        for price in prices[1:]:
            # 若某天的股票价格price + fee小于之前买入时的花费buy，则选择在这天买入，放弃之前的买入
            if price + fee < buy:
                buy = price + fee
            # 若某天的股票价格price大于之前买入时的花费buy，则选择在这天卖出。不过这个选择未必是全局最优，所以提供了一个反悔的操作，
            # 即 buy = price，如果之后遇到更高的股票价格price，则可认为是在那天卖出的。例如：a < b < c，(c - b) + (b - a) == c - a
            elif price > buy:
                res += price - buy
                buy = price
        return res
