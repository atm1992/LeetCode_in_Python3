# -*- coding: UTF-8 -*-
"""
title: 对角线遍历
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.


Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]


Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
-10^5 <= mat[i][j] <= 10^5
"""
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        模拟。
        对于 m x n 的矩阵，共有 m + n - 1 条对角线，相邻对角线的遍历方向相反，若当前遍历方向为从左下到右上，则下一条对角线的遍历方向为从右上到左下。
        设 各条对角线的编号i的范围为 [0, m+n-2] ，则可以看出 编号i = 行下标 + 列下标。右斜对角线是横纵坐标之和为定值；左斜对角线是横纵坐标之差为定值。
        当编号i为偶数时，对角线的方向为从左下到右上。此时行下标逐渐减1，列下标逐渐加1，直到矩阵的边缘为止。
            当 i < m 时，每次都是从第一列开始向斜上方走，即 起始的列下标为0，因此起始的行下标为i-0；
            当 i >= m 时，每次都是从最后一行开始向斜上方走，即 起始的行下标为m-1，因此起始的列下标为i-m+1。
            无论上述哪种情况，走到边缘时，要么行下标为0，要么列下标为n-1。当列下标为n-1时，行下标为i-n+1
            所以，对于对角线i，其行下标的变化为：min(i, m-1) ——> max(0, i-n+1)，逐渐减1
        当编号i为奇数时，对角线的方向为从右上到左下。此时行下标逐渐加1，列下标逐渐减1，直到矩阵的边缘为止。
            当 i < n 时，每次都是从第一行开始向斜下方走，即 起始的行下标为0，因此起始的列下标为i-0；
            当 i >= n 时，每次都是从最后一列开始向斜下方走，即 起始的列下标为n-1，因此起始的行下标为i-n+1。
            无论上述哪种情况，走到边缘时，要么行下标为m-1，要么列下标为0。当列下标为0时，行下标为i
            所以，对于对角线i，其行下标的变化为：max(0, i-n+1) ——> min(m-1, i)，逐渐加1
        """
        res = []
        m, n = len(mat), len(mat[0])
        for i in range(m + n - 1):
            if i & 1:
                for r in range(max(0, i - n + 1), min(m - 1, i) + 1):
                    res.append(mat[r][i - r])
            else:
                for r in range(min(i, m - 1), max(0, i - n + 1) - 1, -1):
                    res.append(mat[r][i - r])
        return res


if __name__ == '__main__':
    print(Solution().findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
