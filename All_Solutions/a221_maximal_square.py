# -*- coding: UTF-8 -*-
"""
title: 最大正方形
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.


Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0


Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """暴力法。会超时"""
        m, n = len(matrix), len(matrix[0])
        max_side = 0
        for i in range(m):
            for j in range(n):
                # 遇到一个 1，则将其作为正方形的左上角
                if matrix[i][j] == '1':
                    max_side = max(max_side, 1)
                    cur_max_side = min(m - i, n - j)
                    # 逐渐在右边增加一列，下边增加一行
                    for k in range(1, cur_max_side):
                        flag = True
                        if matrix[i + k][j + k] == '0':
                            break
                        # 注意变量命名，m/n在前面已经被使用了
                        for h in range(k):
                            if matrix[i + k][j + h] == '0' or matrix[i + h][j + k] == '0':
                                flag = False
                                break
                        if not flag:
                            break
                        max_side = max(max_side, k + 1)
        return max_side * max_side

    def maximalSquare_2(self, matrix: List[List[str]]) -> int:
        """
        动态规划。
        dp[i][j] 表示以点(i,j)为右下角的正方形的最大边长。
        若当前点(i,j)为 '0'，则 dp[i][j] = 0
        若当前点(i,j)为 '1'，则 dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1。
        min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) 表示三个正方形取交集
        边界条件：若当前点(i,j)为 '1'，并且 i == 0 或 j == 0，则 dp[i][j] = 1
        """
        max_side = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side * max_side


if __name__ == '__main__':
    print(Solution().maximalSquare_2(
        [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
