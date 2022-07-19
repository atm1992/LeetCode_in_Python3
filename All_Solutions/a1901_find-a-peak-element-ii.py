# -*- coding: UTF-8 -*-
"""
title: 寻找峰值 II
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.
Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].
You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.
You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.


Example 1:
Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.

Example 2:
Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]
Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.


Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 500
1 <= mat[i][j] <= 10^5
No two adjacent cells are equal.
"""
from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        """二分查找。LeetCode题162的进阶"""

        def get_max_col(row: int) -> int:
            """线性查找输入行row中的最大值所在列"""
            max_col, max_num = 0, mat[row][0]
            for col in range(1, n):
                if mat[row][col] > max_num:
                    max_num = mat[row][col]
                    max_col = col
            return max_col

        m, n = len(mat), len(mat[0])
        low, high = 0, m - 1
        # 退出循环时，low == high，也就确定了最终的峰值所在行
        while low < high:
            mid_row = (low + high) // 2
            # 线性查找mid_row中的最大值所在列
            max_col = get_max_col(mid_row)
            # 接下来，在该最大值所在列，查找可能的峰值所在行
            # mid_row 取不到 high，即 mid_row < m - 1，所以 mid_row+1 < m
            if mat[mid_row][max_col] < mat[mid_row + 1][max_col]:
                # 此时的mid_row不可能是峰值所在行
                low = mid_row + 1
            else:
                # 此时 mat[mid_row][max_col] > mat[mid_row+1][max_col]，因为 No two adjacent cells are equal.
                # 此时的mid_row有可能是峰值所在行
                high = mid_row
        return [low, get_max_col(low)]


if __name__ == '__main__':
    print(Solution().findPeakGrid(mat=[[10, 20, 15], [21, 30, 14], [7, 16, 32]]))
