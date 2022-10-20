# -*- coding: UTF-8 -*-
"""
title: 最大人工岛
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
Return the size of the largest island in grid after applying this operation.
An island is a 4-directionally connected group of 1s.


Example 1:
Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:
Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example 3:
Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.


Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
"""
from collections import defaultdict
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        DFS + 标记岛屿 + 合并岛屿
        使用tag对每个岛屿进行标记，tag可以是DFS起点的坐标，例如：tag = i * n + j + 1，后面加1是为了避免起点为(0, 0)时，tag = 0。
        因为需要使用tag = 0来表示尚未被标记的单元格。DFS遍历计算岛屿的面积，并把属于该岛屿的所有单元格都标记上同一个tag。
        找到grid中所有为0的单元格，将其初始面积设为1，然后遍历4个方向，看看是否存在岛屿，若存在，则把它们合并进来，累加得到最终合并后的面积。
        """

        def dfs(i: int, j: int, tag: int) -> None:
            tags[i][j] = tag
            tag2area[tag] += 1
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                # tags[x][y] != tag 是为了避免重复标记。tags[x][y] 要么为tag，要么为0，不可能是其它值
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 1 and tags[x][y] != tag:
                    dfs(x, y, tag)

        n = len(grid)
        tags = [[0] * n for _ in range(n)]
        tag2area = defaultdict(int)
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                # 发现了尚未被标记的新大陆
                if num == 1 and tags[i][j] == 0:
                    dfs(i, j, i * n + j + 1)

        # 当grid中的单元格已经全部为1时，下面的for循环不会进行计算
        res = max(tag2area.values(), default=0)
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if num == 0:
                    tmp = 1
                    visited_tags = set()
                    for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if 0 <= x < n and 0 <= y < n and grid[x][y] == 1 and tags[x][y] not in visited_tags:
                            tmp += tag2area[tags[x][y]]
                            visited_tags.add(tags[x][y])
                    res = max(res, tmp)
        return res


if __name__ == '__main__':
    print(Solution().largestIsland([[1, 0], [0, 1]]))
