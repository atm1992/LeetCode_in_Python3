# -*- coding: UTF-8 -*-
"""
title: 至少有一个 1 的最左端列
A row-sorted binary matrix means that all elements are 0 or 1 and each row of the matrix is sorted in non-decreasing order.
Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of the leftmost column with a 1 in it. If such an index does not exist, return -1.
You can't access the Binary Matrix directly. You may only access the matrix using a BinaryMatrix interface:
    BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
    BinaryMatrix.dimensions() returns the dimensions of the matrix as a list of 2 elements [rows, cols], which means the matrix is rows x cols.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.
For custom testing purposes, the input will be the entire binary matrix mat. You will not have access to the binary matrix directly.


Example 1:
Input: mat = [[0,0],[1,1]]
Output: 0

Example 2:
Input: mat = [[0,0],[0,1]]
Output: 1

Example 3:
Input: mat = [[0,0],[0,0]]
Output: -1


Constraints:
rows == mat.length
cols == mat[i].length
1 <= rows, cols <= 100
mat[i][j] is either 0 or 1.
mat[i] is sorted in non-decreasing order.
"""


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        """二分查找。时间复杂度为O(mlogn)"""
        m, n = binaryMatrix.dimensions()
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            flag = False
            for i in range(m):
                if binaryMatrix.get(i, mid):
                    flag = True
                    break
            if flag:
                right = mid
            else:
                left = mid + 1
        return -1 if left == n else left

    def leftMostColumnWithOne_2(self, binaryMatrix: 'BinaryMatrix') -> int:
        """从右下角往左上角验证，若当前单元格为1，则往左走；若当前单元格为0，则往上走。时间复杂度为O(m + n)"""
        m, n = binaryMatrix.dimensions()
        r, c = m - 1, n - 1
        res = -1
        while r >= 0 and c >= 0:
            if binaryMatrix.get(r, c):
                res = c
                c -= 1
            else:
                r -= 1
        return res
