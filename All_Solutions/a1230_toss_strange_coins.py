# -*- coding: UTF-8 -*-
"""
title: 抛掷硬币
You have some coins. The i-th coin has a probability prob[i] of facing heads when tossed.
Return the probability that the number of coins facing heads equals target if you toss every coin exactly once.


Example 1:
Input: prob = [0.4], target = 1
Output: 0.40000

Example 2:
Input: prob = [0.5,0.5,0.5,0.5,0.5], target = 0
Output: 0.03125


Constraints:
1 <= prob.length <= 1000
0 <= prob[i] <= 1
0 <= target <= prob.length
Answers will be accepted as correct if they are within 10^-5 of the correct answer.
"""
from typing import List


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        """
        动态规划
        假设 dp[i][j] 表示前i枚硬币中，正面朝上的硬币数量为j的概率。
        状态转移方程：
        当j == 0时，dp[i][0] = dp[i-1][0] * (1 - prob[i])
        当j > 0时，dp[i][j] = dp[i-1][j] * (1 - prob[i]) + dp[i-1][j-1] * prob[i]
        初始值：
        0枚硬币中，正面朝上的硬币数量等于0的概率 dp[0][0] = 1.0
        0枚硬币中，正面朝上的硬币数量大于0的概率 dp[0][j>0] = 0.0
        """
        dp = [1.0] + [0.0] * target
        for p in prob:
            for j in range(target, 0, -1):
                dp[j] = dp[j] * (1 - p) + dp[j - 1] * p
            dp[0] = dp[0] * (1 - p)
        return dp[-1]


if __name__ == '__main__':
    print(Solution().probabilityOfHeads(prob=[0.5, 0.5, 0.5, 0.5, 0.5], target=0))
