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
        """
        动态规划。在任意一天结束时，都一定是以下5种状态之一：
        1、截止到当天，尚未进行任何操作；目前为止，最大利润一直为0，因此无需考虑该状态，直接忽略这些天
        2、截止到当天，完成了第一次买入(可能是今天买入，也可能是之前某天买入)；假设最大利润为buy1，则buy1 = max(buy1', -prices[i])。
        buy1' 表示是之前某天买入，-prices[i] 表示是今天买入。此时利润<=0，是因为买入需要付出成本。
        3、截止到当天，完成了第一次卖出(可能是今天卖出，也可能是之前某天卖出)；假设最大利润为sell1，则sell1 = max(sell1', buy1' + prices[i]),
        buy1' + prices[i] 表示是今天卖出，其中buy1'表示之前某天买入时的最大利润
        4、截止到当天，完成了第二次买入(可能是今天买入，也可能是之前某天买入)；假设最大利润为buy2，则buy2 = max(buy2', sell1' - prices[i])
        5、截止到当天，完成了第二次卖出(可能是今天卖出，也可能是之前某天卖出)。假设最大利润为sell2，则sell2 = max(sell2', buy2' + prices[i])。
        考虑边界情况：
        1、当天买入、卖出，不会影响最终答案，因为该操作带来的利润为0。因此可将状态转移方程改为，这4个方程逐个向下转移：
        buy1 = max(buy1, -prices[i])
        sell1 = max(sell1, buy1 + prices[i])        # buy1相比之前的buy1'，多考虑的是在当天买入的情况，若是当天买入，然后再当天卖出，则此时利润为0，sell1 不可能小于0，因此对sell1的结果没有影响
        buy2 = max(buy2, sell1 - prices[i])         # sell1相比之前的sell1'，多考虑的是在当天卖出的情况，若是当天卖出，然后再当天买入，则此时的sell1 - prices[i] == buy1，而buy2不可能小于buy1，因此对buy2的结果没有影响
        sell2 = max(sell2, buy2 + prices[i])        # buy2相比之前的buy2'，多考虑的是在当天买入的情况，若是当天买入，然后再当天卖出，则此时的buy2 + prices[i] == sell1，而sell2不可能小于sell1，因此对sell2的结果没有影响
        2、初始值，i = 0时的取值：
        buy1 = -prices[0]           # 买入
        sell1 = 0                   # 当天买入，然后再当天卖出
        buy2 = -prices[0]           # 当天买入，再当天卖出，然后再当天买入
        sell2 = 0                   # 当天买入，当天卖出，当天买入，当天卖出
        3、由于动态规划结束后，不超过两笔交易，因此最终答案为 max(0, sell1, sell2)。但因为sell1、sell2的初始值就为0，因此sell1、sell2不可能小于0。
        另外，即使最优情况是只进行一笔交易，那么也可以通过当天买入、然后再当天卖出的方式，将最大利润从sell1转移到sell2。因此，最终答案为sell2
        """
        buy1 = buy2 = -prices[0]
        sell1 = sell2 = 0
        for price in prices[1:]:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)
        return sell2

    def maxProfit_2(self, prices: List[int]) -> int:
        n = len(prices)
        # 第一笔交易时，买入、卖出时的最大利润
        dp_1 = [[0, 0] for _ in range(n)]
        # 第二笔交易时，买入、卖出时的最大利润
        dp_2 = [[0, 0] for _ in range(n)]
        for i in range(n):
            if i == 0:
                dp_1[i][0] = -prices[i]
                dp_2[i][0] = -prices[i]
            else:
                dp_1[i][0] = max(dp_1[i - 1][0], -prices[i])
                dp_1[i][1] = max(dp_1[i - 1][1], dp_1[i - 1][0] + prices[i])
                dp_2[i][0] = max(dp_2[i - 1][0], dp_1[i - 1][1] - prices[i])
                dp_2[i][1] = max(dp_2[i - 1][1], dp_2[i - 1][0] + prices[i])
        return dp_2[-1][1]


if __name__ == '__main__':
    print(Solution().maxProfit_2([7, 6, 4, 3, 1]))
