# -*- coding: UTF-8 -*-
"""
title: 太平洋大西洋水流问题
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.


Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Example 2:
Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]


Constraints:
m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 10^5
"""
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """DFS。从左边界、上边界的单元格开始，DFS查找所有可以流到太平洋的单元格；
        然后从右边界、下边界的单元格开始，DFS查找所有可以流到大西洋的单元格"""
        m, n = len(heights), len(heights[0])
        can_pacific = set()

        def go_pacific(i: int, j: int) -> None:
            can_pacific.add((i, j))
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[i][j] and (x, y) not in can_pacific:
                    go_pacific(x, y)

        # 左边界
        for i in range(m):
            if (i, 0) not in can_pacific:
                go_pacific(i, 0)
        # 上边界
        for j in range(n):
            if (0, j) not in can_pacific:
                go_pacific(0, j)

        can_atlantic = set()
        res = []

        def go_atlantic(i: int, j: int) -> None:
            can_atlantic.add((i, j))
            if (i, j) in can_pacific:
                res.append((i, j))
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[i][j] and (x, y) not in can_atlantic:
                    go_atlantic(x, y)

        # 右边界
        for i in range(m):
            if (i, n - 1) not in can_atlantic:
                go_atlantic(i, n - 1)
        # 下边界
        for j in range(n):
            if (m - 1, j) not in can_atlantic:
                go_atlantic(m - 1, j)
        return res


if __name__ == '__main__':
    print(Solution().pacificAtlantic(
        heights=[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
