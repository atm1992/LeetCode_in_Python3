# -*- coding: UTF-8 -*-
"""
title: 岛屿的最大面积
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.


Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""
from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """DFS"""

        def dfs(i: int, j: int) -> int:
            res = 1
            grid[i][j] = 2
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    res += dfs(x, y)
            return res

        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        # 恢复原始的grid。或者也可以deepcopy一个grid再去dfs
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 2:
        #             grid[i][j] = 1
        return res

    def maxAreaOfIsland_2(self, grid: List[List[int]]) -> int:
        """BFS"""
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                tmp_res = 0
                queue = deque([(i, j)])
                while queue:
                    cur_i, cur_j = queue.popleft()
                    # 同一个坐标(cur_i, cur_j)，有可能会被先后重复加入到queue，所以这里需要判断
                    if grid[cur_i][cur_j] != 1:
                        continue
                    tmp_res += 1
                    grid[cur_i][cur_j] = 2
                    for x, y in [(cur_i - 1, cur_j), (cur_i + 1, cur_j), (cur_i, cur_j - 1), (cur_i, cur_j + 1)]:
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                            queue.append((x, y))
                res = max(res, tmp_res)
        return res


if __name__ == '__main__':
    print(Solution().maxAreaOfIsland_2(
        grid=[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
              [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
