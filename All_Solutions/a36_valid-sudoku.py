# -*- coding: UTF-8 -*-
"""
title: 有效的数独
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """使用hashmap来计数，但考虑到数独中的数字为1~9，所以可节省些空间，使用数组来计数，数组下标(0~8)分别对应数独中的数字(1~9)。
        rows/columns两个二维数组分别统计每行/每列中数字的出现次数，sub_boxes三维数组用来统计3 x 3小方块中数字的出现次数。
        只要某个数字的出现次数大于1，就可直接return False"""
        # 数独的长宽是固定的 9 x 9
        rows = [[0] * 9 for _ in range(9)]
        columns = [[0] * 9 for _ in range(9)]
        sub_boxes = [[[0] * 9 for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch != '.':
                    # ch的取值范围为: '1' ~ '9'
                    idx = int(ch) - 1
                    rows[i][idx] += 1
                    columns[j][idx] += 1
                    sub_boxes[i // 3][j // 3][idx] += 1
                    if rows[i][idx] > 1 or columns[j][idx] > 1 or sub_boxes[i // 3][j // 3][idx] > 1:
                        return False
        return True
