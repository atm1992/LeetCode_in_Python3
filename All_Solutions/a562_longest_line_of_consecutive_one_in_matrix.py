# -*- coding: UTF-8 -*-
"""
title: 矩阵中最长的连续1线段
Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.
The line could be horizontal, vertical, diagonal, or anti-diagonal.


Example 1:
Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
Output: 3

Example 2:
Input: mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
Output: 4


Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
mat[i][j] is either 0 or 1.
"""
from typing import List


class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        """
        动态规划
        dp_h[i][j] 表示在horizontal方向上以坐标(i, j)结尾的连续1线段的长度
        dp_v[i][j] 表示在vertical方向上以坐标(i, j)结尾的连续1线段的长度
        dp_d[i][j] 表示在diagonal方向上以坐标(i, j)结尾的连续1线段的长度
        dp_ad[i][j] 表示在anti-diagonal方向上以坐标(i, j)结尾的连续1线段的长度
        状态转移方程：
        dp_h[i][j] = 0 if mat[i][j] == 0 else dp_h[i][j-1] + 1
        dp_v[i][j] = 0 if mat[i][j] == 0 else dp_v[i-1][j] + 1
        dp_d[i][j] = 0 if mat[i][j] == 0 else dp_d[i-1][j-1] + 1
        dp_ad[i][j] = 0 if mat[i][j] == 0 else dp_ad[i-1][j+1] + 1
        """
        res = 0
        n = len(mat[0])
        dp_h = [0] * (n + 2)
        dp_v = [0] * (n + 2)
        dp_d = [0] * (n + 2)
        dp_ad = [0] * (n + 2)
        for row in mat:
            pre_dp_d = 0
            for j, num in enumerate(row, 1):
                cur_dp_d = dp_d[j]
                dp_h[j] = 0 if num == 0 else dp_h[j - 1] + 1
                dp_v[j] = 0 if num == 0 else dp_v[j] + 1
                dp_d[j] = 0 if num == 0 else pre_dp_d + 1
                dp_ad[j] = 0 if num == 0 else dp_ad[j + 1] + 1
                pre_dp_d = cur_dp_d
                res = max(res, dp_h[j], dp_v[j], dp_d[j], dp_ad[j])
        return res


if __name__ == '__main__':
    print(Solution().longestLine([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]))
