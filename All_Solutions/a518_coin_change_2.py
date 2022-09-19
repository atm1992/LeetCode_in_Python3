# -*- coding: UTF-8 -*-
"""
title: 零钱兑换 II
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.


Example 1:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1


Constraints:
1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
"""
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        动态规划
        假设dp[i]表示凑成总金额i的硬币组合数，[c0, c1, ……, cn-1] 表示可选的n种硬币面值。
        状态转移方程为：dp[i] += dp[i-c]，其中的c表示凑成总金额i的最后一枚硬币
        边界条件：dp[0] = 1，当amount为0时，只有1种组合，就是一枚硬币都不选
        """
        dp = [1] + [0] * amount
        # 不会存在重复计算的情况，因为外层循环每次枚举的都是不同硬币，而内层循环是使用当前硬币来凑成总金额coin ~ amount，
        # 把总金额coin ~ amount都计算一遍后，再退到外层循环，枚举下一枚硬币。因此每个组合中的硬币顺序都与coins中的顺序相同。
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[-1]


if __name__ == '__main__':
    print(Solution().change(amount=5, coins=[1, 2, 5]))
