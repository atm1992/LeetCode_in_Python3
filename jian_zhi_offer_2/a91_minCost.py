# -*- coding: UTF-8 -*-
"""
title: 粉刷房子
假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。
当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x 3 的正整数矩阵 costs 来表示的。
例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2] 表示第 1 号房子粉刷成绿色的花费，以此类推。
请计算出粉刷完所有房子最少的花费成本。


示例 1：
输入: costs = [[17,2,17],[16,16,5],[14,3,19]]
输出: 10
解释: 将 0 号房子粉刷成蓝色，1 号房子粉刷成绿色，2 号房子粉刷成蓝色。
     最少花费: 2 + 5 + 3 = 10。

示例 2：
输入: costs = [[7,6,2]]
输出: 2


提示:
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
