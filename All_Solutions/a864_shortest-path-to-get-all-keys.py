# -*- coding: UTF-8 -*-
"""
title: 获取所有钥匙的最短路径
You are given an m x n grid grid where:
    '.' is an empty cell.
    '#' is a wall.
    '@' is the starting point.
    Lowercase letters represent keys.
    Uppercase letters represent locks.
You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.
If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.
For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.
Return the lowest number of moves to acquire all keys. If it is impossible, return -1.


Example 1:
Input: grid = ["@.a..","###.#","b.A.B"]
Output: 8
Explanation: Note that the goal is to obtain all the keys not to open all the locks.

Example 2:
Input: grid = ["@..aA","..B#.","....b"]
Output: 6

Example 3:
Input: grid = ["@Aa"]
Output: -1


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either an English letter, '.', '#', or '@'.
The number of keys in the grid is in the range [1, 6].
Each key in the grid is unique.
Each key in the grid has a matching lock.
"""
from collections import deque
from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        """状态压缩 + BFS。使用一个数字state来表示钥匙状态，假设当前遇到钥匙b，则state的右侧第二位变为1"""
        m, n = len(grid), len(grid[0])
        start = (0, 0)
        # The number of keys in the grid is in the range [1, 6]，所以 1 <= key_cnt <= 6
        key_cnt = 0
        for i in range(m):
            for j in range(n):
                ch = grid[i][j]
                if ch == '@':
                    start = (i, j)
                elif ch.islower():
                    key_cnt += 1
        # 横坐标、纵坐标、钥匙状态、路径长度
        queue = deque([(start[0], start[1], 0, 0)])
        # 横坐标、纵坐标、钥匙状态
        visited = {(start[0], start[1], 0)}
        while queue:
            i, j, state, length = queue.popleft()
            length += 1
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] != '#':
                    ch = grid[x][y]
                    # 遇到了锁，但没有钥匙
                    if ch.isupper() and (state >> (ord(ch) - ord('A'))) & 1 == 0:
                        continue
                    next_state = state
                    # 遇到了钥匙
                    if ch.islower():
                        next_state = state | 1 << (ord(ch) - ord('a'))
                        if next_state == 2 ** key_cnt - 1:
                            return length
                    # 同一种钥匙状态没必要两次经过同一个单元格
                    if (x, y, next_state) not in visited:
                        visited.add((x, y, next_state))
                        queue.append((x, y, next_state, length))
        return -1


if __name__ == '__main__':
    print(Solution().shortestPathAllKeys(grid=["@..aA", "..B#.", "....b"]))
