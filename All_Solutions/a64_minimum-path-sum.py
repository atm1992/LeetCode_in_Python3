# -*- coding: UTF-8 -*-
"""
title：最小路径和
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.


Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """二维动态规划"""
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        # 从最后一行开始填写dp数组
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i == rows - 1 and j == cols - 1:
                    dp[i][j] = grid[i][j]
                elif i == rows - 1 and j < cols - 1:
                    dp[i][j] = grid[i][j] + dp[i][j + 1]
                elif i < rows - 1 and j == cols - 1:
                    dp[i][j] = grid[i][j] + dp[i + 1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]

    def minPathSum_2(self, grid: List[List[int]]) -> int:
        """二维动态规划（直接在原矩阵中修改，不需要使用额外存储空间）。从左上角走到右下角，最终返回右下角位置的值"""
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]
