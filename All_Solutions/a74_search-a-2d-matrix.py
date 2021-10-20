# -*- coding: UTF-8 -*-
"""
title: 搜索二维矩阵
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.


Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """两次二分查找。先按行二分，再按列二分"""
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m - 1
        row = -1
        while left <= right:
            mid = (left + right) // 2
            l, r = matrix[mid][0], matrix[mid][n - 1]
            if l <= target <= r:
                row = mid
                break
            elif r < target:
                left = mid + 1
            else:
                right = mid - 1
        if row > -1:
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                tmp = matrix[row][mid]
                if tmp == target:
                    return True
                elif tmp < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

    def searchMatrix_2(self, matrix: List[List[int]], target: int) -> bool:
        """一次二分查找"""
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            tmp = matrix[mid // n][mid % n]
            if tmp == target:
                return True
            elif tmp < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


if __name__ == '__main__':
    print(Solution().searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))
