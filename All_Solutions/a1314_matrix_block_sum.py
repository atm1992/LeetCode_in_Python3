# -*- coding: UTF-8 -*-
"""
title: 矩阵区域和
Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:
    i - k <= r <= i + k,
    j - k <= c <= j + k, and
    (r, c) is a valid position in the matrix.


Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]

Example 2:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]


Constraints:
m == mat.length
n == mat[i].length
1 <= m, n, k <= 100
1 <= mat[i][j] <= 100
"""
from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """二维前缀和。参考LeetCode题304"""
        m, n = len(mat), len(mat[0])
        pre_mat = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre_mat[i][j] = pre_mat[i - 1][j] + pre_mat[i][j - 1] + mat[i - 1][j - 1] - pre_mat[i - 1][j - 1]
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                min_r, max_r = max(i - k, 0), min(i + k, m - 1) + 1
                min_c, max_c = max(j - k, 0), min(j + k, n - 1) + 1
                # 右下角矩形的面积 = 整体面积 - 上面面积 - 左边面积 + 左上面积
                res[i][j] = pre_mat[max_r][max_c] - pre_mat[min_r][max_c] - pre_mat[max_r][min_c] + pre_mat[min_r][min_c]
        return res


if __name__ == '__main__':
    print(Solution().matrixBlockSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=2))
