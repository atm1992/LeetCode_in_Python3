# -*- coding: UTF-8 -*-
"""
title: 岛屿的最大面积
给定一个由 0 和 1 组成的非空二维数组 grid ，用来表示海洋岛屿地图。
一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
找到给定的二维数组中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。


示例 1:
输入: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
输出: 6
解释: 对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。

示例 2:
输入: grid = [[0,0,0,0,0,0,0,0]]
输出: 0


提示：
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1
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
