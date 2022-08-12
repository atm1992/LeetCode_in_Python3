# -*- coding: UTF-8 -*-
"""
title: 旋转图像
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Example 3:
Input: matrix = [[1]]
Output: [[1]]

Example 4:
Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]


Constraints:
matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        使用辅助矩阵。旋转规律：对于矩阵中第 i 行的第 j 个元素，在旋转后，它出现在倒数第 i 列的第 j 个位置。
        即 matrix[i][j] ——> matrix[j][n-1-i]
        """
        n = len(matrix)
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_new[j][n - 1 - i] = matrix[i][j]
        # 不能写成 matrix = matrix_new。修改变量matrix中保存的地址所指向的内容，而并不修改变量matrix中保存的地址
        matrix[:] = matrix_new

    def rotate_2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        使用翻转代替旋转。顺时针旋转90度 等价于 先水平轴翻转，再主对角线翻转。可以用Example 2为例尝试下。
        水平轴翻转：matrix[i][j] <——> matrix[n-1-i][j]
        主对角线翻转：matrix[i][j] <——> matrix[j][i]
        上面的两个等式联立，其实就是上面的：matrix[i][j] ——> matrix[j][n-1-i]
        """
        n = len(matrix)
        # 水平轴翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]

        # 主对角线翻转
        for i in range(1, n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
