# -*- coding: UTF-8 -*-
"""
title: 二维子矩阵的和
给定一个二维矩阵 matrix，以下类型的多个请求：
    计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。
实现 NumMatrix 类：
    NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化
    int sumRegion(int row1, int col1, int row2, int col2) 返回左上角 (row1, col1) 、右下角 (row2, col2) 的子矩阵的元素总和。


示例 1：
输入:
["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
输出:
[null, 8, 11, 12]
解释:
NumMatrix numMatrix = new NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (红色矩形框的元素总和)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (绿色矩形框的元素总和)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (蓝色矩形框的元素总和)


提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-10^5 <= matrix[i][j] <= 10^5
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
最多调用 10^4 次 sumRegion 方法
"""
from typing import List


class NumMatrix:
    """一维前缀和"""

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
    """二维前缀和。dp[i][j] 表示以(0,0)为左上角，以(i,j)为右下角的矩形区域的总和"""

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        dp_matrix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp_matrix[i + 1][j + 1] = dp_matrix[i + 1][j] + dp_matrix[i][j + 1] - dp_matrix[i][j] + matrix[i][j]
        self.dp_matrix = dp_matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        matrix = self.dp_matrix
        return matrix[row2 + 1][col2 + 1] - matrix[row2 + 1][col1] - matrix[row1][col2 + 1] + matrix[row1][col1]


if __name__ == '__main__':
    obj = NumMatrix2([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print(obj.sumRegion(1, 1, 2, 2))
