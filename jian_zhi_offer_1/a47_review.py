# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        """动态规划"""
        m, n = len(grid), len(grid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j]) + grid[i][j]
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().maxValue([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]))
