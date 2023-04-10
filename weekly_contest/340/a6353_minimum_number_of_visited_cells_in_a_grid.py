# -*- coding: utf-8 -*-
# @date: 2023/4/9
# @author: liuquan
"""
title: 网格图中最少访问的格子数
You are given a 0-indexed m x n integer matrix grid. Your initial position is at the top-left cell (0, 0).
Starting from the cell (i, j), you can move to one of the following cells:
    Cells (i, k) with j < k <= grid[i][j] + j (rightward movement), or
    Cells (k, j) with i < k <= grid[i][j] + i (downward movement).
Return the minimum number of cells you need to visit to reach the bottom-right cell (m - 1, n - 1). If there is no valid path, return -1.


Example 1:
Input: grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]
Output: 4
Explanation: The image above shows one of the paths that visits exactly 4 cells.

Example 2:
Input: grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]
Output: 3
Explanation: The image above shows one of the paths that visits exactly 3 cells.

Example 3:
Input: grid = [[2,1,0],[1,0,0]]
Output: -1
Explanation: It can be proven that no path exists.


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10^5
1 <= m * n <= 10^5
0 <= grid[i][j] < m * n
grid[m - 1][n - 1] == 0
"""
import heapq
from typing import List


class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        """m + n 个优先队列(最小堆)"""
        m, n = len(grid), len(grid[0])
        dist = [[-1] * n for _ in range(m)]
        dist[0][0] = 1
        rows, cols = [[] for _ in range(m)], [[] for _ in range(n)]
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if num == 0 and (i, j) != (m - 1, n - 1):
                    continue
                while rows[i] and rows[i][0][1] < j:
                    heapq.heappop(rows[i])
                if rows[i]:
                    dist[i][j] = rows[i][0][0] + 1 if dist[i][j] == -1 else min(dist[i][j], rows[i][0][0] + 1)

                while cols[j] and cols[j][0][1] < i:
                    heapq.heappop(cols[j])
                if cols[j]:
                    dist[i][j] = cols[j][0][0] + 1 if dist[i][j] == -1 else min(dist[i][j], cols[j][0][0] + 1)

                # 值为0的格子对于后面的格子没有意义，因为没法向后传递
                if dist[i][j] != -1 and num > 0:
                    # 注意：这里是num + j，而不是num + i，表示的是最多能够传递到第i行的第num + j列
                    heapq.heappush(rows[i], (dist[i][j], num + j))
                    heapq.heappush(cols[j], (dist[i][j], num + i))
        return dist[m - 1][n - 1]


if __name__ == '__main__':
    print(Solution().minimumVisitedCells(grid=[[3, 4, 2, 1], [4, 2, 3, 1], [2, 1, 0, 0], [2, 4, 0, 0]]))
