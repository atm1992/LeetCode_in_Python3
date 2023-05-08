# -*- coding: utf-8 -*-
# @date: 2023/5/8
# @author: liuquan
"""
title: 推箱子
A storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.
The game is represented by an m x n grid of characters grid where each element is a wall, floor, or box.
Your task is to move the box 'B' to the target position 'T' under the following rules:
    The character 'S' represents the player. The player can move up, down, left, right in grid if it is a floor (empty cell).
    The character '.' represents the floor which means a free cell to walk.
    The character '#' represents the wall which means an obstacle (impossible to walk there).
    There is only one box 'B' and one target cell 'T' in the grid.
    The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a push.
    The player cannot walk through the box.
Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return -1.


Example 1:
Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 3
Explanation: We return only the number of times the box is pushed.

Example 2:
Input: grid = [["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#","#","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: -1

Example 3:
Input: grid = [["#","#","#","#","#","#"],
               ["#","T",".",".","#","#"],
               ["#",".","#","B",".","#"],
               ["#",".",".",".",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]]
Output: 5
Explanation: push the box down, left, left, up and up.


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid contains only characters '.', '#', 'S', 'T', or 'B'.
There is only one character 'S', 'B', and 'T' in the grid.
"""
from collections import deque
from typing import List


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        """
        DFS + 双端队列，即 0-1 DFS
        1、先找到player和box的坐标，为方便处理，可将坐标(i, j)转换为 i * n + j
        2、使用一个双端队列来记录 (p_pos, b_pos, step)，并使用一个(m*n) * (m*n)的二维数组来记录 (p_pos, b_pos) 是否已访问过。数组的效率比哈希表的效率更高
            2_1、若p_pos的下一个位置(上、下、左、右)等于b_pos，则说明推了一次箱子，step + 1，加入到双端队列的末尾
            2_2、若p_pos的下一个位置不等于b_pos，则说明没有推动箱子，step不变，加入到双端队列的开头
            注意：此过程中，需判断p_pos的下一个位置是否合法(未越界、且不等于'#')，若推动了箱子，则还需判断箱子的下一个位置是否合法。
            另外，加入到双端队列之前，需判断 (p_pos, b_pos) 是否已访问过
        """
        m, n = len(grid), len(grid[0])
        p_pos = b_pos = t_pos = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    p_pos = i * n + j
                elif grid[i][j] == 'B':
                    b_pos = i * n + j
                elif grid[i][j] == 'T':
                    t_pos = i * n + j
        visited = [[False] * m * n for _ in range(m * n)]
        visited[p_pos][b_pos] = True
        queue = deque([(p_pos, b_pos, 0)])
        while queue:
            p_pos, b_pos, step = queue.popleft()
            if b_pos == t_pos:
                return step
            i, j = divmod(p_pos, n)
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] != '#':
                    if x * n + y == b_pos:
                        # 箱子的下一个位置与(i, j)关于(x, y)对称
                        b_i, b_j = 2 * x - i, 2 * y - j
                        if 0 <= b_i < m and 0 <= b_j < n and grid[b_i][b_j] != '#' and not visited[b_pos][
                            b_i * n + b_j]:
                            visited[b_pos][b_i * n + b_j] = True
                            queue.append((b_pos, b_i * n + b_j, step + 1))
                    elif not visited[x * n + y][b_pos]:
                        visited[x * n + y][b_pos] = True
                        queue.appendleft((x * n + y, b_pos, step))
        return -1


if __name__ == '__main__':
    print(Solution().minPushBox(grid=[["#", "#", "#", "#", "#", "#"],
                                      ["#", "T", ".", ".", "#", "#"],
                                      ["#", ".", "#", "B", ".", "#"],
                                      ["#", ".", ".", ".", ".", "#"],
                                      ["#", ".", ".", ".", "S", "#"],
                                      ["#", "#", "#", "#", "#", "#"]]))
