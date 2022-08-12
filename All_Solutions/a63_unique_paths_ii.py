# -*- coding: UTF-8 -*-
"""
title：不同路径 II
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and space is marked as 1 and 0 respectively in the grid.


Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 

Constraints:
m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """动态规划。需要考虑起点或终点有障碍物的情况，此时的结果直接为0"""
        # 这里是为了更快的返回结果，其实下面的for循环能够处理这种情况
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # 只用一行来记录dp结果，使用了滚动数组(状态压缩)来降低空间复杂度。每个元素表示从起点(0,0)到for循环中当前行的该列有多少条路径。
        dp = [0] * n
        # obstacleGrid[0][0]上肯定没有障碍物，否则上面就return了，因此将从起点(0,0)到起点(0,0)的路径数初始化为1
        dp[0] = 1
        # 先计算第1行所有列的路径数 …… 最后计算第m行所有列的路径数
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    # 一旦发现当前单元格有障碍物，则从起点到该点的路径数直接清0，因为所有路径都无法通过该点
                    dp[j] = 0
                    continue
                if j > 0 and not obstacleGrid[i][j - 1]:
                    # 将 dp[i][j] = dp[i][j-1] + dp[i-1][j] 简化成了dp[j] = dp[j-1]，因为dp[i][j]包含了dp[i-1][j]，dp[j]是逐行演变计算过来的，
                    # 所以只需加上从当前单元格右边单元格过来的路径数
                    dp[j] += dp[j - 1]
        return dp[-1]
