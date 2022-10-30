# -*- coding: UTF-8 -*-
"""
title: 岛屿的周长
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:
Input: grid = [[1]]
Output: 4

Example 3:
Input: grid = [[1,0]]
Output: 4


Constraints:
row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.
"""
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        迭代。推荐此方法
        对于一个陆地格子来说，它的某条边会被计入周长，当且仅当这条边相邻的是水域格子或边界。
        """
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    tmp = 0
                    for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if not 0 <= x < m or not 0 <= y < n or grid[x][y] == 0:
                            tmp += 1
                    res += tmp
        return res

    def islandPerimeter_2(self, grid: List[List[int]]) -> int:
        """DFS"""

        def dfs(i: int, j: int) -> int:
            if not 0 <= i < m or not 0 <= j < n or grid[i][j] == 0:
                return 1
            # 已经遍历过该格子
            if grid[i][j] == 2:
                return 0
            grid[i][j] = 2
            res = 0
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                res += dfs(x, y)
            return res

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # There is exactly one island in grid.
                    return dfs(i, j)


if __name__ == '__main__':
    print(Solution().islandPerimeter_2(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
