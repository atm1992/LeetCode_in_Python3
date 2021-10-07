# -*- coding: UTF-8 -*-
"""
title: N皇后 II
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.


Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
Input: n = 1
Output: 1


Constraints:
1 <= n <= 9
皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        """回溯。从左上到右下方向的斜线(diagonal_1)，行下标(row)减去列下标(col)的结果是固定的；
        从右上到左下方向的斜线(diagonal_2)，行下标(row)加上列下标(col)的结果是固定的"""

        def dfs(row: int = 0) -> int:
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if col in forbidden_idx['column'] or row - col in forbidden_idx['diagonal_1'] or row + col in \
                        forbidden_idx['diagonal_2']:
                    continue
                forbidden_idx['column'].append(col)
                forbidden_idx['diagonal_1'].append(row - col)
                forbidden_idx['diagonal_2'].append(row + col)
                count += dfs(row + 1)
                forbidden_idx['column'].pop(-1)
                forbidden_idx['diagonal_1'].pop(-1)
                forbidden_idx['diagonal_2'].pop(-1)
            return count

        forbidden_idx = {
            'column': [],
            'diagonal_1': [],
            'diagonal_2': []
        }
        return dfs()


if __name__ == '__main__':
    print(Solution().totalNQueens(4))
