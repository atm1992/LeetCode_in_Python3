# -*- coding: UTF-8 -*-
"""
title: 最短的桥
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.
An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.
You may change 0's to 1's to connect the two islands to form one island.
Return the smallest number of 0's you must flip to connect the two islands.


Example 1:
Input: grid = [[0,1],[1,0]]
Output: 1

Example 2:
Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:
Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1


Constraints:
n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
"""
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        DFS + BFS
        原问题等价于计算两个岛之间的最短距离。先使用DFS找到其中一座岛，将该岛的所有单元格都标记为2，然后再使用BFS对这座岛不断地向外一圈一圈延伸，
        当遍历到1时，所延伸的圈数就是所求的最短距离。
        """

        def dfs(i: int, j: int, path: list) -> None:
            grid[i][j] = 2
            path.append((i, j))
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                    dfs(x, y, path)

        n = len(grid)
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if num != 1:
                    continue
                queue = []
                dfs(i, j, queue)
                step = 0
                while True:
                    tmp = queue
                    queue = []
                    for a, b in tmp:
                        for x, y in [(a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)]:
                            if 0 <= x < n and 0 <= y < n:
                                if grid[x][y] == 0:
                                    grid[x][y] = 2
                                    queue.append((x, y))
                                elif grid[x][y] == 1:
                                    return step
                    step += 1


if __name__ == '__main__':
    print(Solution().shortestBridge(grid=[[0, 1, 0], [0, 0, 0], [0, 0, 1]]))
