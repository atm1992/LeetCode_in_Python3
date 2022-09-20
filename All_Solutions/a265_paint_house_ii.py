# -*- coding: UTF-8 -*-
"""
title: 粉刷房子 II
There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
The cost of painting each house with a certain color is represented by an n x k cost matrix costs.
    For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on...
Return the minimum cost to paint all houses.


Example 1:
Input: costs = [[1,5,3],[2,9,4]]
Output: 5
Explanation:
Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5;
Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.

Example 2:
Input: costs = [[1,3],[2,4]]
Output: 5


Constraints:
costs.length == n
costs[i].length == k
1 <= n <= 100
2 <= k <= 20
1 <= costs[i][j] <= 20

Follow up: Could you solve it in O(nk) runtime?
"""
from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        """
        动态规划。
        dp[i][j] 表示将 house i 刷成 color j 的最少花费
        状态转移方程：dp[i][j] = costs[i][j] + min(dp[i-1][0], ……, dp[i-1][j-1], dp[i-1][j+1], ……, dp[i-1][k-1])
        边界条件：dp[0][j] = costs[0][j]
        """
        n, k = len(costs), len(costs[0])
        dp = costs[0].copy()
        for i in range(1, n):
            # min_1 - 最小值；min_2 - 次小值。这两个值可以是相等的
            if dp[0] < dp[1]:
                min_1, min_2 = dp[0], dp[1]
            else:
                min_1, min_2 = dp[1], dp[0]
            for j in range(2, k):
                if dp[j] < min_1:
                    min_1, min_2 = dp[j], min_1
                elif dp[j] < min_2:
                    min_2 = dp[j]
            for j in range(k):
                dp[j] = costs[i][j] + (min_1 if dp[j] != min_1 else min_2)
        return min(dp)


if __name__ == '__main__':
    print(Solution().minCostII(costs=[[1, 5, 3], [2, 9, 4]]))
