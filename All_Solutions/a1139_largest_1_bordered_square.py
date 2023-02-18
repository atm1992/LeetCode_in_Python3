# -*- coding: UTF-8 -*-
"""
title: 最大的以 1 为边界的正方形
Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't exist in the grid.


Example 1:
Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 9

Example 2:
Input: grid = [[1,1,0,0]]
Output: 1


Constraints:
1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] is 0 or 1
"""
from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        """
        动态规划
        dp[i][j][0] 表示grid[i-1][j-1]左侧连续1的个数，若grid[i-1][j-1]=0，则dp[i][j][0]=0
        dp[i][j][1] 表示grid[i-1][j-1]上侧连续1的个数，若grid[i-1][j-1]=0，则dp[i][j][1]=0
        """
        m, n = len(grid), len(grid[0])
        dp = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if grid[i - 1][j - 1] == 0:
                    continue
                dp[i][j][0] = dp[i][j - 1][0] + 1
                dp[i][j][1] = dp[i - 1][j][1] + 1
                tmp = min(dp[i][j])
                while tmp > res and (dp[i][j - tmp + 1][1] < tmp or dp[i - tmp + 1][j][0] < tmp):
                    tmp -= 1
                if tmp > res:
                    res = tmp
        return res * res


if __name__ == '__main__':
    print(Solution().largest1BorderedSquare(grid=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
