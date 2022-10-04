# -*- coding: UTF-8 -*-
"""
title: 轰炸敌人
Given an m x n matrix grid where each cell is either a wall 'W', an enemy 'E' or empty '0', return the maximum enemies you can kill using one bomb. You can only place the bomb in an empty cell.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since it is too strong to be destroyed.


Example 1:
Input: grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3

Example 2:
Input: grid = [["W","W","W"],["0","0","0"],["E","E","E"]]
Output: 1


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 'W', 'E', or '0'.
"""
from typing import List


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        """
        动态规划
        从左上角扫描一次grid，然后再从右下角扫描一次grid
        假设 dp[i][j][0] 表示坐标(i, j)正上方的敌人数量，dp[i][j][1] 表示坐标(i, j)正左侧的敌人数量，dp[i][j][2] 表示坐标(i, j)正下方的敌人数量，dp[i][j][3] 表示坐标(i, j)正右侧的敌人数量。
        正上方：dp[i][j][0] = dp[i - 1][j][0] + (1 if grid[i - 1][j] == 'E' else 0) if i > 0 and grid[i - 1][j] != 'W' else 0
        正左侧：dp[i][j][1] = dp[i][j - 1][1] + (1 if grid[i][j - 1] == 'E' else 0) if j > 0 and grid[i][j - 1] != 'W' else 0
        正下方：dp[i][j][2] = dp[i + 1][j][2] + (1 if grid[i + 1][j] == 'E' else 0) if i < m - 1 and grid[i + 1][j] != 'W' else 0
        正右侧：dp[i][j][3] = dp[i][j + 1][3] + (1 if grid[i][j + 1] == 'E' else 0) if j < n - 1 and grid[i][j + 1] != 'W' else 0
        """
        res = 0
        m, n = len(grid), len(grid[0])
        dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i > 0 and grid[i - 1][j] != 'W':
                    dp[i][j][0] = dp[i - 1][j][0] + (1 if grid[i - 1][j] == 'E' else 0)
                if j > 0 and grid[i][j - 1] != 'W':
                    dp[i][j][1] = dp[i][j - 1][1] + (1 if grid[i][j - 1] == 'E' else 0)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1 and grid[i + 1][j] != 'W':
                    dp[i][j][2] = dp[i + 1][j][2] + (1 if grid[i + 1][j] == 'E' else 0)
                if j < n - 1 and grid[i][j + 1] != 'W':
                    dp[i][j][3] = dp[i][j + 1][3] + (1 if grid[i][j + 1] == 'E' else 0)
                if grid[i][j] == '0':
                    res = max(res, sum(dp[i][j]))
        return res


if __name__ == '__main__':
    print(Solution().maxKilledEnemies([["W", "W", "W"], ["0", "0", "0"], ["E", "E", "E"]]))
