# -*- coding: UTF-8 -*-
"""
title: 粉刷房子
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.
For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
Return the minimum cost to paint all houses.


Example 1:
Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.

Example 2:
Input: costs = [[7,6,2]]
Output: 2


Constraints:
costs.length == n
costs[i].length == 3
1 <= n <= 100
1 <= costs[i][j] <= 20
"""
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        动态规划。
        dp[i][0] 表示将第i间房子刷成红色的最少花费；dp[i][1] 表示将第i间房子刷成蓝色的最少花费；dp[i][2] 表示将第i间房子刷成绿色的最少花费。
        状态转移方程：dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
        边界条件：dp[0] = costs[0]
        """
        # 1 <= n
        red_0, blue_1, green_2 = costs[0]
        for cur_0, cur_1, cur_2 in costs[1:]:
            red_0, blue_1, green_2 = cur_0 + min(blue_1, green_2), cur_1 + min(red_0, green_2), cur_2 + min(red_0, blue_1)
        return min(red_0, blue_1, green_2)


if __name__ == '__main__':
    print(Solution().minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]))
