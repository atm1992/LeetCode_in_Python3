# -*- coding: UTF-8 -*-
"""
title: 二维区域和检索 - 矩阵不可变
Given a 2D matrix matrix, handle multiple queries of the following type:
    Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:
    NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
    int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).


Example 1:
Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]
Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)


Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-10^5 <= matrix[i][j] <= 10^5
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 10^4 calls will be made to sumRegion.
"""
from typing import List


class NumMatrix:
    """一维前缀和。对原二维矩阵matrix中的每一行都构建一个前缀和数组"""

    def __init__(self, matrix: List[List[int]]):
        pre_matrix = []
        for row in matrix:
            tmp = [0]
            for num in row:
                tmp.append(tmp[-1] + num)
            pre_matrix.append(tmp)
        self.pre_matrix = pre_matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for row in range(row1, row2 + 1):
            res += self.pre_matrix[row][col2 + 1] - self.pre_matrix[row][col1]
        return res


class NumMatrix2:
    """二维前缀和。将每次检索的时间复杂度降为O(1)"""

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        pre_matrix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre_matrix[i][j] = pre_matrix[i - 1][j] + pre_matrix[i][j - 1] + matrix[i - 1][j - 1] - \
                                   pre_matrix[i - 1][j - 1]
        self.pre_matrix = pre_matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # 右下角矩形的面积 = 整体面积 - 上面面积 - 左边面积 + 左上面积
        return self.pre_matrix[row2 + 1][col2 + 1] - self.pre_matrix[row1][col2 + 1] - self.pre_matrix[row2 + 1][col1] + self.pre_matrix[row1][col1]


if __name__ == '__main__':
    obj = NumMatrix2([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print(obj.sumRegion(1, 1, 2, 2))
