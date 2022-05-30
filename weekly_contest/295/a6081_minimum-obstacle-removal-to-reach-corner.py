# -*- coding: UTF-8 -*-
"""
title: 到达角落需要移除障碍物的最小数目
You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:
    0 represents an empty cell,
    1 represents an obstacle that may be removed.
You can move up, down, left, or right from and to an empty cell.
Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).


Example 1:
Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
Output: 2
Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
It can be shown that we need to remove at least 2 obstacles, so we return 2.
Note that there may be other ways to remove 2 obstacles to create a path.

Example 2:
Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
Output: 0
Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10^5
2 <= m * n <= 10^5
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0
"""
import heapq
from collections import deque
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        """
        Dijkstra 算法，使用优先队列。参考LeetCode题1368方法一
        把障碍物当作可以经过的单元格，经过障碍物单元格的代价为1，经过空白单元格的代价为0。
        原问题转化为从起点(0, 0)到终点(m-1, n-1)的最短路径问题。
        """
        m, n = len(grid), len(grid[0])
        # 总共有m*n个节点，所有节点到达(0, 0)的最短带权路径长度都不会超过 m + n。初始起点(0, 0)到达(0, 0)的最短路径长度为0
        # 每次循环都能确定一个节点到达(0, 0)的最短路径长度，然后每次都pop当前路径长度最短的那个节点，所以需要使用优先队列
        # dist 数组其实也可使用二维数组，转成一维数组后，访问下标需要从 [i][j] 转换为 [i * n + j]
        dist = [0] + [m + n] * (m * n - 1)
        # dist, i, j。按照每个节点到达(0, 0)的最短路径长度dist进行升序
        queue = [(0, 0, 0)]
        while queue:
            cur_dist, i, j = heapq.heappop(queue)
            for x, y in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                if 0 <= x < m and 0 <= y < n:
                    new_pos = x * n + y
                    new_dist = cur_dist + grid[x][y]
                    if new_dist < dist[new_pos]:
                        dist[new_pos] = new_dist
                        heapq.heappush(queue, (new_dist, x, y))
        return dist[-1]

    def minimumObstacles_2(self, grid: List[List[int]]) -> int:
        """0-1 BFS，使用双端队列。参考LeetCode题1368方法二"""
        m, n = len(grid), len(grid[0])
        dist = [0] + [m + n] * (m * n - 1)
        queue = deque([(0, 0)])
        while queue:
            i, j = queue.popleft()
            cur_pos = i * n + j
            for x, y in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                if 0 <= x < m and 0 <= y < n:
                    new_pos = x * n + y
                    new_dist = dist[cur_pos] + grid[x][y]
                    if new_dist < dist[new_pos]:
                        dist[new_pos] = new_dist
                        if grid[x][y] == 0:
                            queue.appendleft((x, y))
                        else:
                            queue.append((x, y))
        return dist[-1]
