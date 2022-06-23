# -*- coding: UTF-8 -*-
"""
title: 01 矩阵
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.


Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]


Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""
from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """BFS。BFS可以找到从起点到其余所有点的最短距离"""
        m, n = len(mat), len(mat[0])
        res = [[0] * n for _ in range(m)]
        zeroes = [(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0]
        queue = deque(zeroes)
        visited = set(zeroes)
        while queue:
            i, j = queue.popleft()
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    res[x][y] = res[i][j] + 1
                    queue.append((x, y))
                    visited.add((x, y))
        return res

    def updateMatrix_2(self, mat: List[List[int]]) -> List[List[int]]:
        """
        动态规划。
        dp[i][j] 表示从位置(i, j)到最近的0的距离。这个最近的0可能在(i, j)的左上方、左下方、右上方、右下方，正上方包含在左上方、右上方以内。
        假设最近的0在(i, j)的左上方，则状态转移方程为：dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        其它三种方向，状态转移方程类似
        """
        m, n = len(mat), len(mat[0])
        # 1 <= m * n <= 10^4，mat 中至少有一个 0
        dp = [[10 ** 4] * n for _ in range(m)]
        # 先找到所有的0，将其距离更新为0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
        # 假设最近的0在(i, j)的左上方，注意i、j的遍历顺序
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
        # 假设最近的0在(i, j)的左下方，注意i、j的遍历顺序
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if i + 1 < m:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
        # 假设最近的0在(i, j)的右上方，注意i、j的遍历顺序
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if i - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                if j + 1 < n:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
        # 假设最近的0在(i, j)的右下方，注意i、j的遍历顺序
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j + 1 < n:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
        return dp

    def updateMatrix_3(self, mat: List[List[int]]) -> List[List[int]]:
        """
        动态规划。方法二中存在重复计算，其实只需计算两个方向即可，(左上 + 右下) 或 (左下 + 右上)
        以(左上 + 右下)为例：
        假设y表示正确值，n表示错误值，?表示未判断。
        初始时，矩阵中有3个0：
        ? ? ? ? ? ? ? ? ?
        ? ? ? ? ? ? 0 ? ?
        ? ? ? ? ? ? ? ? ?
        ? ? ? ? 0 ? ? ? ?
        ? ? 0 ? ? ? ? ? ?
        ? ? ? ? ? ? ? ? ?
        从左上角开始更新值，以左上方元素为基准：
        n n n n n n n n n
        n n n n n n 0 y y
        n n n n n n y y y
        n n n n 0 y y y y
        n n 0 y y y y y y
        n n y y y y y y y
        从右下角开始更新值，以右下方元素为基准：
        y y y y y y y y y
        y y y y y y 0 y y
        y y y y y y y y y
        y y y y 0 y y y y
        y y 0 y y y y y y
        y y y y y y y y y
        """
        m, n = len(mat), len(mat[0])
        # 1 <= m * n <= 10^4，mat 中至少有一个 0
        dp = [[10 ** 4] * n for _ in range(m)]
        # 先找到所有的0，将其距离更新为0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
        # 假设最近的0在(i, j)的左上方，注意i、j的遍历顺序
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
        # 假设最近的0在(i, j)的右下方，注意i、j的遍历顺序
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j + 1 < n:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
        return dp
