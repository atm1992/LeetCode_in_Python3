# -*- coding: UTF-8 -*-
"""
title: 生命游戏
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
    Any live cell with fewer than two live neighbors dies as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.


Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]


Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.

Follow up:
Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?
"""
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        对于1来说，只需关注它的邻居中有多少个1，若不是2个或3个，则变为0，否则不变。
        对于0来说，只需关注它的邻居中有多少个1，若等于3个，则变为1，否则不变。
        复制一份原始数组用作参考，然后直接在原始数组中更新值。
        """
        m, n = len(board), len(board[0])
        duplicate = [[board[i][j] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                cnt_1 = 0
                for x, y in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1),
                             (i + 1, j), (i + 1, j + 1)]:
                    if 0 <= x < m and 0 <= y < n and duplicate[x][y]:
                        cnt_1 += 1
                if duplicate[i][j]:
                    if cnt_1 not in [2, 3]:
                        board[i][j] = 0
                else:
                    if cnt_1 == 3:
                        board[i][j] = 1

    def gameOfLife_2(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        对于1来说，只需关注它的邻居中有多少个1，若不是2个或3个，则变为0，否则不变。
        对于0来说，只需关注它的邻居中有多少个1，若等于3个，则变为1，否则不变。
        位运算原地操作。原始值0、1只使用了int的最低位，可以借助int的倒数第2位来表示在第二次遍历时，是否需要将原始值取反。
        例如：
        原始值为1，即 01，若之后需要变为0，则在第一次遍历时，将原始值修改为11，最低位依旧还是原始值1；
        原始值为0，即 00，若之后需要变为1，则在第一次遍历时，将原始值修改为10，最低位依旧还是原始值0。
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                cnt_1 = 0
                for x, y in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1),
                             (i + 1, j), (i + 1, j + 1)]:
                    if 0 <= x < m and 0 <= y < n and board[x][y] & 1:
                        cnt_1 += 1
                if board[i][j]:
                    if cnt_1 not in [2, 3]:
                        # 不写成 board[i][j] |= 2，是避免多次从board中取值
                        board[i][j] = 3
                else:
                    if cnt_1 == 3:
                        board[i][j] = 2

        for i in range(m):
            for j in range(n):
                tmp = board[i][j]
                if tmp in [2, 3]:
                    board[i][j] = 0 if tmp == 3 else 1
