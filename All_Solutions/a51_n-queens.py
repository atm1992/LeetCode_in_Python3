# -*- coding: UTF-8 -*-
"""
title: N皇后
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.


Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]


Constraints:
1 <= n <= 9
皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """回溯。从左上到右下方向的斜线(diagonal_1)，行下标(row)减去列下标(col)的结果是固定的；
        从右上到左下方向的斜线(diagonal_2)，行下标(row)加上列下标(col)的结果是固定的"""

        def dfs(row: int = 0, chessboard: List[str] = []):
            if row == n:
                res.append(chessboard[:])
                return
            for col in range(n):
                if col in forbidden_idx['column'] or row - col in forbidden_idx['diagonal_1'] or row + col in \
                        forbidden_idx['diagonal_2']:
                    continue
                forbidden_idx['column'].append(col)
                forbidden_idx['diagonal_1'].append(row - col)
                forbidden_idx['diagonal_2'].append(row + col)
                chessboard.append('.' * col + 'Q' + '.' * (n - 1 - col))
                dfs(row + 1, chessboard)
                chessboard.pop(-1)
                forbidden_idx['column'].pop(-1)
                forbidden_idx['diagonal_1'].pop(-1)
                forbidden_idx['diagonal_2'].pop(-1)

        forbidden_idx = {
            'column': [],
            'diagonal_1': [],
            'diagonal_2': []
        }
        res = []
        dfs()
        return res


if __name__ == '__main__':
    print(Solution().solveNQueens(9))
