# -*- coding: UTF-8 -*-
"""
title: 不同岛屿的数量
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.
Return the number of distinct islands.


Example 1:
Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 1

Example 2:
Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
Output: 3


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""
from copy import deepcopy
from typing import List, Tuple


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        """
        DFS 搜索出所有的岛屿，难点在于如何判断两个岛屿是否相同。
        判断两个岛屿是否相同：
        将组成岛屿的所有单元格坐标 平移到 左上角(0, 0)，然后将平移后的所有单元格坐标放入一个数组，最后通过set集合去重。
        例如：原始坐标为：[(1, 2), (2, 1), (2, 2)]，平移后：[(0, 0), (1, -1), (1, 0)]。注意：平移后的坐标可以存在负数
        对于相同形状的岛屿，DFS从左上角开始访问的路径顺序是确定的
        """
        m, n = len(grid), len(grid[0])
        copy_grid = deepcopy(grid)
        # 虽然每次都是从左上角开始访问，但因为岛屿的形状是不规则的，所以在之后的DFS过程中，依旧有可能往左、往上走
        # 例如岛屿的形状为：[(1, 2), (2, 1), (2, 2), (2, 3), (2, 4), (1, 4)]
        # 注意：对方向的遍历顺序有要求，必须是 右、下、左、上 [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # 或 上、左、下、右 [(-1, 0), (0, -1), (1, 0), (0, 1)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(grid: List[List[int]], i: int, j: int, relative_x: int, relative_y: int,
                shape: List[Tuple[int, int]]) -> None:
            shape.append((relative_x, relative_y))
            # 走过的单元格将会被永久修改为0，不会再被改回1，所以在前面会 deepcopy(grid)
            grid[i][j] = 0
            for delta_x, delta_y in directions:
                x = i + delta_x
                y = j + delta_y
                relative_x += delta_x
                relative_y += delta_y
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    dfs(grid, x, y, relative_x, relative_y, shape)

        res = set()
        for i in range(m):
            for j in range(n):
                # 将当前单元格作为岛屿的左上角，左上角的相对坐标为(0, 0)
                if copy_grid[i][j] == 1:
                    shape = []
                    dfs(copy_grid, i, j, 0, 0, shape)
                    res.add(tuple(shape))

        return len(res)


if __name__ == '__main__':
    print(Solution().numDistinctIslands([[0, 0, 1], [0, 0, 1], [1, 1, 0]]))
