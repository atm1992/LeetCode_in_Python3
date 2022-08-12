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
from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        # 若所有位置都在边界，则无需进行任何替换
        if m < 3 or n < 3:
            return

        que = deque()

        for i in range(m):
            # 第一列
            if board[i][0] == 'O':
                que.append((i, 0))
                board[i][0] = '#'
            # 最后一列
            if board[i][n - 1] == 'O':
                que.append((i, n - 1))
                board[i][n - 1] = '#'

        for i in range(1, n - 1):
            # 第一行
            if board[0][i] == 'O':
                que.append((0, i))
                board[0][i] = '#'
            # 最后一行
            if board[m - 1][i] == 'O':
                que.append((m - 1, i))
                board[m - 1][i] = '#'

        while que:
            x, y = que.popleft()
            for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] == 'O':
                    que.append((new_x, new_y))
                    board[new_x][new_y] = '#'

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
