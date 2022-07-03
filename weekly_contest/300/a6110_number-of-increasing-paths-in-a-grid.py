# -*- coding: UTF-8 -*-
"""
title: 网格图中递增路径的数目
You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.
Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. Since the answer may be very large, return it modulo 10^9 + 7.
Two paths are considered different if they do not have exactly the same sequence of visited cells.


Example 1:
Input: grid = [[1,1],[3,4]]
Output: 8
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [1], [3], [4].
- Paths with length 2: [1 -> 3], [1 -> 4], [3 -> 4].
- Paths with length 3: [1 -> 3 -> 4].
The total number of paths is 4 + 3 + 1 = 8.

Example 2:
Input: grid = [[1],[2]]
Output: 3
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [2].
- Paths with length 2: [1 -> 2].
The total number of paths is 2 + 1 = 3.


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 10^5
1 <= grid[i][j] <= 10^5
"""
from collections import deque
from functools import lru_cache
from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        """拓扑排序 + BFS"""
        mod = 10 ** 9 + 7
        res = 0
        m, n = len(grid), len(grid[0])
        in_degree = [[0] * n for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] < val:
                        in_degree[i][j] += 1
                if in_degree[i][j] == 0:
                    queue.append((i, j))
        dp = [[0] * n for _ in range(m)]
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                val = grid[i][j]
                for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if not (0 <= x < m and 0 <= y < n):
                        continue
                    if grid[x][y] > val:
                        in_degree[x][y] -= 1
                        if in_degree[x][y] == 0:
                            # (x, y)将作为(i, j)的下一层
                            queue.append((x, y))
                    if grid[x][y] < val:
                        dp[i][j] = (dp[i][j] + dp[x][y]) % mod
                # [val] 单独作为一条递增路径
                dp[i][j] += 1
                res = (res + dp[i][j]) % mod
        return res

    def countPaths_2(self, grid: List[List[int]]) -> int:
        """DFS + 记忆化。遍历每个单元格，以这个单元格为起点，往上、下、左、右四个方向前进，若下一个单元格的值比当前单元格的值大，则可以前进。"""
        mod = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])

        @lru_cache(maxsize=m * n)
        def dfs(i: int, j: int) -> int:
            """返回以单元格grid[i][j]为起点的递增路径数"""
            # [grid[i][j]] 可以单独作为一条递增路径
            cnt = 1
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] > grid[i][j]:
                    cnt = (cnt + dfs(x, y)) % mod
            return cnt

        res = 0
        for i in range(m):
            for j in range(n):
                res = (res + dfs(i, j)) % mod
        return res


if __name__ == '__main__':
    print(Solution().countPaths_2(grid=[[1], [2]]))
