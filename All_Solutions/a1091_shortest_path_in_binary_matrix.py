# -*- coding: UTF-8 -*-
"""
title: 二进制矩阵中的最短路径
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
    All the visited cells of the path are 0.
    All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.


Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1


Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""
from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """BFS最短路问题"""
        if grid[0][0] or grid[-1][-1]:
            return -1
        n = len(grid)
        if n == 1:
            return 1
        queue = deque([(0, 0)])
        # 若允许修改输入数组，也可以在append到队列后，将grid[x][y]的值改为1，这样就不需要使用visited了
        visited = {(0, 0)}
        res = 1
        while queue:
            res += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for x, y in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1),
                             (i + 1, j), (i + 1, j + 1)]:
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0 and (x, y) not in visited:
                        if x == n - 1 and y == n - 1:
                            return res
                        queue.append((x, y))
                        visited.add((x, y))
        return -1
