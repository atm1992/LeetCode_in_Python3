# -*- coding: UTF-8 -*-
"""
title: 搜索二维矩阵 II
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.


Example 1:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false


Constraints:
m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-10^9 <= matrix[i][j] <= 10^9
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-10^9 <= target <= 10^9
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """二分查找"""
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                mid_val = matrix[i][mid]
                if mid_val == target:
                    return True
                elif mid_val > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return False

    def searchMatrix_2(self, matrix: List[List[int]], target: int) -> bool:
        """Z字形查找。从右上角开始搜索，若值小于target，则说明可以排除第一行，因为最右侧的值是当前行的最大值，所以向下走一行；
        若值大于target，则说明可以排除最后一列，因为最上方的值是当前列的最小值，所以向左走一列。"""
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            val = matrix[i][j]
            if val == target:
                return True
            elif val < target:
                i += 1
            else:
                j -= 1
        return False


if __name__ == '__main__':
    print(Solution().searchMatrix(
        matrix=[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
        target=20))
