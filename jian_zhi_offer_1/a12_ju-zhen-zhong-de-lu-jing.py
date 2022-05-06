# -*- coding: UTF-8 -*-
"""
title: 矩阵中的路径
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。


示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2：
输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false


提示：
1 <= board.length <= 200
1 <= board[i].length <= 200
board 和 word 仅由大小写英文字母组成
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """回溯"""
        def check(i: int, j: int, idx: int) -> None:
            nonlocal flag
            if board[i][j] != word[idx]:
                return
            # 注意这个判断条件和上面那个判断条件之间的顺序，例如：board=[["a"]], word="a"
            if idx == size - 1:
                flag = True
                return
            ch = board[i][j]
            board[i][j] = '#'
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and board[x][y] != '#':
                    check(x, y, idx + 1)
                    if flag:
                        # 这里不能写return，因为之后还需要恢复board
                        break
            board[i][j] = ch

        m, n = len(board), len(board[0])
        size = len(word)
        flag = False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    check(i, j, 0)
                    if flag:
                        return True
        return False


if __name__ == '__main__':
    print(Solution().exist(board=[["a"]], word="a"))
