# -*- coding: UTF-8 -*-
"""
title: 卖木头块
You are given two integers m and n that represent the height and width of a rectangular piece of wood. You are also given a 2D integer array prices, where prices[i] = [hi, wi, pricei] indicates you can sell a rectangular piece of wood of height hi and width wi for pricei dollars.
To cut a piece of wood, you must make a vertical or horizontal cut across the entire height or width of the piece to split it into two smaller pieces. After cutting a piece of wood into some number of smaller pieces, you can sell pieces according to prices. You may sell multiple pieces of the same shape, and you do not have to sell all the shapes. The grain of the wood makes a difference, so you cannot rotate a piece to swap its height and width.
Return the maximum money you can earn after cutting an m x n piece of wood.
Note that you can cut the piece of wood as many times as you want.


Example 1:
Input: m = 3, n = 5, prices = [[1,4,2],[2,2,7],[2,1,3]]
Output: 19
Explanation: The diagram above shows a possible scenario. It consists of:
- 2 pieces of wood shaped 2 x 2, selling for a price of 2 * 7 = 14.
- 1 piece of wood shaped 2 x 1, selling for a price of 1 * 3 = 3.
- 1 piece of wood shaped 1 x 4, selling for a price of 1 * 2 = 2.
This obtains a total of 14 + 3 + 2 = 19 money earned.
It can be shown that 19 is the maximum amount of money that can be earned.

Example 2:
Input: m = 4, n = 6, prices = [[3,2,10],[1,4,2],[4,1,3]]
Output: 32
Explanation: The diagram above shows a possible scenario. It consists of:
- 3 pieces of wood shaped 3 x 2, selling for a price of 3 * 10 = 30.
- 1 piece of wood shaped 1 x 4, selling for a price of 1 * 2 = 2.
This obtains a total of 30 + 2 = 32 money earned.
It can be shown that 32 is the maximum amount of money that can be earned.
Notice that we cannot rotate the 1 x 4 piece of wood to obtain a 4 x 1 piece of wood.


Constraints:
1 <= m, n <= 200
1 <= prices.length <= 2 * 10^4
prices[i].length == 3
1 <= hi <= m
1 <= wi <= n
1 <= pricei <= 10^6
All the shapes of wood (hi, wi) are pairwise distinct.
"""
from typing import List


class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        """
        动态规划
        dp[i][j] 表示将一块高i、宽j的木块，切割后能得到的最多钱数。最终答案为dp[m][n]
        分为3种切割方式：
        1、不切割，直接售卖，如果prices中存在的话，不存在的话，价格算作0
        2、水平切割，将高i切分为k和i-k，此时 dp[i][j] = max(dp[k][j] + dp[i-k][j])，1 <= k <= i-1
        3、垂直切割，将宽j切分为k和j-k，此时 dp[i][j] = max(dp[i][k] + dp[i][j-k])，1 <= k <= j-1
        上述3种情况取最大值，即为最终的 dp[i][j]
        """
        shape2price = {(h, w): p for h, w, p in prices}
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                r1 = shape2price.get((i, j), 0)
                r2 = 0
                for k in range(1, i):
                    r2 = max(r2, dp[k][j] + dp[i - k][j])
                r3 = 0
                for k in range(1, j):
                    r3 = max(r3, dp[i][k] + dp[i][j - k])
                dp[i][j] = max(r1, r2, r3)
        return dp[-1][-1]

    def sellingWood_2(self, m: int, n: int, prices: List[List[int]]) -> int:
        """
        动态规划。优化方法一
        1、1 <= k <= i-1、1 <= k <= j-1，根据对称性，可以只枚举一半，即 1 <= k <= i//2、1 <= k <= j//2
        2、shape2price 可以直接记录到dp二维数组中，不需要单独使用一个dict
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for h, w, p in prices:
            dp[h][w] = p
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                r2 = 0
                for k in range(1, i // 2 + 1):
                    r2 = max(r2, dp[k][j] + dp[i - k][j])
                r3 = 0
                for k in range(1, j // 2 + 1):
                    r3 = max(r3, dp[i][k] + dp[i][j - k])
                dp[i][j] = max(dp[i][j], r2, r3)
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().sellingWood(m=4, n=6, prices=[[3, 2, 10], [1, 4, 2], [4, 1, 3]]))
