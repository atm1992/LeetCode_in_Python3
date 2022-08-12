# -*- coding: UTF-8 -*-
"""
title：稀疏矩阵的乘法
Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.


Example 1:
Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
Output: [[7,0,0],[-7,0,3]]

Example 2:
Input: mat1 = [[0]], mat2 = [[0]]
Output: [[0]]


Constraints:
m == mat1.length
k == mat1[i].length == mat2.length
n == mat2[i].length
1 <= m, n, k <= 100
-100 <= mat1[i][j], mat2[i][j] <= 100
"""
from typing import List


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        """
        稀疏矩阵的特点就是矩阵中绝大多数的元素均为0，当mat1[i][j]或mat2[j][k]为0时，可以跳过这些计算
        res[i][j] = mat1[i][0] * mat2[0][j] + mat1[i][1] * mat2[1][j] + ... + mat1[i][k] * mat2[k][j]
        """
        m, l, n = len(mat1), len(mat1[0]), len(mat2[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(l):
                if mat1[i][j] == 0:
                    continue
                for k in range(n):
                    if mat2[j][k] == 0:
                        continue
                    res[i][k] += mat1[i][j] * mat2[j][k]
        return res


if __name__ == '__main__':
    print(Solution().multiply(mat1=[[1, 0, 0], [-1, 0, 3]], mat2=[[7, 0, 0], [0, 0, 0], [0, 0, 1]]))
