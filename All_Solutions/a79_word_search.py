# -*- coding: UTF-8 -*-
"""
title: 单词搜索
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """回溯"""
        m, n = len(board), len(board[0])
        k = len(word)
        if m * n < k:
            return False
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row: int, col: int, idx: int):
            if board[row][col] != word[idx]:
                return False
            if idx == k - 1:
                return True

            # 使用 # 表示该位置已访问过
            store_val = board[row][col]
            board[row][col] = '#'
            flag = False
            for di, dj in directions:
                new_row, new_col = row + di, col + dj
                if 0 <= new_row < m and 0 <= new_col < n and board[new_row][new_col] != '#' and dfs(new_row, new_col,
                                                                                                    idx + 1):
                    flag = True
                    break
            board[row][col] = store_val
            return flag

        # 依次将board中的每个单元格作为起始搜索位置
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    print(Solution().exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED"))
