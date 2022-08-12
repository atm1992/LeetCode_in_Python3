# -*- coding: UTF-8 -*-
"""
title: 矩阵中的最长递增路径
Given an m x n integers matrix, return the length of the longest increasing path in matrix.
From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).


Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:
Input: matrix = [[1]]
Output: 1


Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 2^31 - 1
"""
from collections import deque
from functools import lru_cache
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """DFS + 记忆化。每一个单元格都可作为起点，然后进行DFS，最终返回以这个单元格作为起点的最长路径长度"""
        res = 0
        m, n = len(matrix), len(matrix[0])

        @lru_cache(maxsize=m * n)
        def dfs(i: int, j: int) -> int:
            ret = 1
            val = matrix[i][j]
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > val:
                    ret = max(ret, dfs(x, y) + 1)
            return ret

        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res

    def longestIncreasingPath_2(self, matrix: List[List[int]]) -> int:
        """
        拓扑排序 + BFS。拓扑排序指的是将一个有向无环图(DAG)中的所有顶点排成一个线性序列，这样的一个线性序列就叫拓扑序，
        动态规划的本质其实就是沿着一个拓扑序更新dp数组，因为拓扑序的无环，从而保证了动态规划的无后效性。
        如果一个图不是DAG，那么它肯定不存在拓扑序；如果是DAG，那么至少存在一个拓扑序。反之，如果一个图存在一个拓扑序，那么这个图必定是DAG。
        总结：DAG 与 拓扑序 互为充要条件。
        """
        m, n = len(matrix), len(matrix[0])
        out_degree = [[0] * n for _ in range(m)]
        queue = deque()
        # 计算所有单元格的出度(将每个单元格看作DAG中的一个顶点)。并将所有出度为 0 的单元格加入队列，作为BFS的起点，从路径的终点一直搜索到起点。
        # 当然也可计算所有单元格的入度，然后将所有入度为 0 的单元格加入队列，作为BFS的起点，这样就变成了从路径的起点一直搜索到终点。
        for i in range(m):
            for j in range(n):
                val = matrix[i][j]
                for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > val:
                        out_degree[i][j] += 1
                if out_degree[i][j] == 0:
                    queue.append((i, j))
        res = 0
        # 从出度为 0 的单元格开始一层一层向外搜索，每进入下一层，路径长度就加1。搜索的总层数就是矩阵中最长递增路径的长度
        while queue:
            res += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                val = matrix[i][j]
                for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] < val:
                        # 表示(x, y)无需再考虑比它大的(i, j)这个单元格了，即意味着 (x, y) ——> (i, j) 的这条有向边消失了，所以(x, y)的出度需要减1
                        out_degree[x][y] -= 1
                        if out_degree[x][y] == 0:
                            # (x, y)将作为(i, j)的下一层
                            queue.append((x, y))
        return res
