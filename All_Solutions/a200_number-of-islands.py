# -*- coding: UTF-8 -*-
"""
title: 岛屿数量
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        深度优先搜索。
        扫描整个二维网格。如果一个位置为 1，则以其为起始节点开始进行深度优先搜索。在深度优先搜索的过程中，每个搜索到的 1 都会被重新标记为 0。
        最终岛屿的数量就是我们进行深度优先搜索的次数。
        """
        res = 0
        m, n = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> None:
            grid[i][j] = '0'
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                    dfs(x, y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res

    def numIslands_2(self, grid: List[List[str]]) -> int:
        """
        广度优先搜索。
        扫描整个二维网格。如果一个位置为 1，则以其为起始节点开始进行广度优先搜索。在广度优先搜索的过程中，每个搜索到的 1 都会被重新标记为 0。
        最终岛屿的数量就是我们进行广度优先搜索的次数。
        """
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    grid[i][j] = '0'
                    neighbors = deque([(i, j)])
                    while neighbors:
                        row, col = neighbors.popleft()
                        for x, y in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                                grid[x][y] = '0'
                                neighbors.append((x, y))
        return res


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(Solution().numIslands_2(grid))
