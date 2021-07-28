# -*- coding: UTF-8 -*-
"""
title：被围绕的区域
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.


Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Example 2:
Input: board = [["X"]]
Output: [["X"]]
 

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'
"""
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        rows, cols = len(board), len(board[0])
        # 若所有位置都在边界，则无需进行任何替换
        if rows < 3 or cols < 3:
            return

        def bfs(i, j):
            queue = [(i, j)]
            while queue:
                m, n = queue.pop(0)
                if 0 <= m < rows and 0 <= n < cols and board[m][n] == 'O':
                    board[m][n] = '#'
                    for (x, y) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                        queue.append((m + x, n + y))

        for i in range(rows):
            # 第一列
            if board[i][0] == 'O':
                bfs(i, 0)
            # 最后一列
            if board[i][cols - 1] == 'O':
                bfs(i, cols - 1)

        for j in range(cols):
            # 第一行
            if board[0][j] == 'O':
                bfs(0, j)
            # 最后一行
            if board[rows - 1][j] == 'O':
                bfs(rows - 1, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
