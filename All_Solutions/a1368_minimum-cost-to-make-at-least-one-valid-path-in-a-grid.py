# -*- coding: UTF-8 -*-
"""
title: 使网格图至少有一条有效路径的最小代价
Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:
    1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
    2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
    3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
    4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
Notice that there could be some signs on the cells of the grid that point outside the grid.
You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.
You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.
Return the minimum cost to make the grid have at least one valid path.


Example 1:
Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output: 3
Explanation: You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
The total cost = 3.

Example 2:
Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
Output: 0
Explanation: You can follow the path from (0, 0) to (2, 2).

Example 3:
Input: grid = [[1,2],[4,3]]
Output: 1


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
1 <= grid[i][j] <= 4
"""
import heapq
from collections import deque
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        """
        Dijkstra 算法，使用优先队列。
        求解带非负权图中的单源最短路径，Dijkstra 算法可以求出从某一节点到其余所有节点的最短路径。本题只需求出从 (0, 0) 到 (m-1, n−1) 的最短路径。
        题目分析，若没有 每个格子中的数字只能修改一次 这个条件，则可轻松地将本题转化为一个求解最短路径的问题：
        1、希望求出从 (0, 0) 到 (m-1, n−1) 的最小代价；
        2、对于任意位置 (i, j)，都可向上、下、左、右移动一个位置，但不能走出边界。若移动的位置与 (i, j) 处的箭头方向一致，则移动的代价为 0，否则为 1；
        3、因此，可将数组 grid 建模成一个包含 m*n 个节点和不超过 4*m*n 条边的有向图 G。图 G 中的每一个节点表示数组 grid 中的一个位置，
        它会向不超过 4 个相邻的节点各连出一条边，边的权值要么为 0（移动方向与箭头方向一致），要么为 1（移动方向与箭头方向不一致)；
        4、可在图 G 上使用任意一种最短路径算法，求出从 (0, 0) 到 (m−1, n−1) 的最短路径，即可得到答案。
        其实，加上 每个格子中的数字只能修改一次 这个条件后，仍可使用任意一种最短路径算法来求解最短路径，因为即使用Dijkstra 算法求出的最短路径中包含了重复的位置，
        那么只需删去这两个重复位置之间的所有位置 以及 这两个重复位置之一，就可得到一条符合题目要求的最短路径。
        """
        m, n = len(grid), len(grid[0])
        # 总共有m*n个节点，所有节点到达(0, 0)的最短带权路径长度都不会超过 m + n。初始起点(0, 0)到达(0, 0)的最短路径长度为0
        # 每次循环都能确定一个节点到达(0, 0)的最短路径长度，然后每次都pop当前路径长度最短的那个节点，所以需要使用优先队列
        # dist 数组其实也可使用二维数组，转成一维数组后，访问下标需要从 [i][j] 转换为 [i * n + j]
        dist = [0] + [m + n] * (m * n - 1)
        # dist, i, j。按照每个节点到达(0, 0)的最短路径长度dist进行升序
        queue = [(0, 0, 0)]
        # 用于记录当前有哪些节点已经确定了最短路径长度。其实不用visited数组也可以。不过用了，可以运行更快些。
        # 可使用下面这个示例来验证，确实会存在重复。
        # [[3, 4, 3], [2, 2, 2], [2, 1, 1], [4, 3, 2], [2, 1, 4], [2, 4, 1], [3, 3, 3], [1, 4, 2], [2, 2, 1], [2, 1, 1],
        #          [3, 3, 1], [4, 1, 4], [2, 1, 4], [3, 2, 2], [3, 3, 1], [4, 4, 1], [1, 2, 2], [1, 1, 1], [1, 3, 4], [1, 2, 1],
        #          [2, 2, 4], [2, 1, 3], [1, 2, 1], [4, 3, 2], [3, 3, 4], [2, 2, 1], [3, 4, 3], [4, 2, 3], [4, 4, 4]]
        visited = [False] * (m * n)
        while queue:
            cur_dist, i, j = heapq.heappop(queue)
            cur_pos = i * n + j
            if visited[cur_pos]:
                print('重复: ', cur_pos)
                continue
            visited[cur_pos] = True
            # 当前位置 (i, j) 上的方向
            cur_direction = grid[i][j]
            # enumerate 的起始下标改为从1开始，是为了方便与题目给定的4个方向标识进行匹配。
            # 1 - right；2 - left；3 - bottom；4 - top
            for idx, (x, y) in enumerate([(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)], 1):
                new_pos = x * n + y
                # 若移动的位置与 (i, j) 处的箭头方向一致，则移动的代价为 0，否则为 1
                new_dist = cur_dist + (1 if cur_direction != idx else 0)
                if 0 <= x < m and 0 <= y < n and new_dist < dist[new_pos]:
                    dist[new_pos] = new_dist
                    heapq.heappush(queue, (new_dist, x, y))
        return dist[-1]

    def minCost_2(self, grid: List[List[int]]) -> int:
        """
        0-1 BFS，使用双端队列。
        常规的BFS可以找出边权均为 1 时的单源最短路径，保证BFS正确性的基础在于：对于源点 s 以及任意两个节点 u 和 v，
        如果 dist(s,u) < dist(s,v)（dist(x,y) 表示从节点 x 到节点 y 的最短路径长度），那么节点 u 一定会比节点 v 先被pop出队列。
        在常规的BFS中，是使用队列来保证从队首到队尾的所有节点，它们与源点之间的距离是单调递增的。
        但是，如果边权不完全为1，还存在0，那么可使用双端队列来维护节点之间的顺序，当任一节点 u 被pop出队列时，如果它到某节点 v_i 有一条权值为 0 的边，
        那么就将节点 v_i 加入到双端队列的队首。如果它到某节点 v_j 有一条权值为 1 的边，那么就和常规的BFS一样，将节点 v_j 加入双端队列的队尾。
        这样一来，就可以保证任意时刻从队首到队尾的所有节点，它们与源点之间的距离是单调递增的。
        与常规的BFS相比，在 0-1 BFS 中，每个节点最多被添加进双端队列两次(队首一次、队尾一次)；而在常规的BFS中，每个节点最多被添加进队列一次。
        """
        m, n = len(grid), len(grid[0])
        dist = [0] + [m + n] * (m * n - 1)
        queue = deque([(0, 0)])
        # 用于记录当前有哪些节点已经确定了最短路径长度。其实不用visited数组也可以。不过用了，可以运行更快些。
        # 可使用下面这个示例来验证，确实会存在重复。
        # [[3, 4, 3], [2, 2, 2], [2, 1, 1], [4, 3, 2], [2, 1, 4], [2, 4, 1], [3, 3, 3], [1, 4, 2], [2, 2, 1], [2, 1, 1],
        #          [3, 3, 1], [4, 1, 4], [2, 1, 4], [3, 2, 2], [3, 3, 1], [4, 4, 1], [1, 2, 2], [1, 1, 1], [1, 3, 4], [1, 2, 1],
        #          [2, 2, 4], [2, 1, 3], [1, 2, 1], [4, 3, 2], [3, 3, 4], [2, 2, 1], [3, 4, 3], [4, 2, 3], [4, 4, 4]]
        visited = [False] * (m * n)
        while queue:
            i, j = queue.popleft()
            cur_pos = i * n + j
            if visited[cur_pos]:
                print('重复: ', cur_pos)
                continue
            visited[cur_pos] = True
            cur_direction = grid[i][j]
            for idx, (x, y) in enumerate([(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)], 1):
                new_pos = x * n + y
                new_dist = dist[cur_pos] + (1 if cur_direction != idx else 0)
                if 0 <= x < m and 0 <= y < n and new_dist < dist[new_pos]:
                    dist[new_pos] = new_dist
                    if cur_direction == idx:
                        queue.appendleft((x, y))
                    else:
                        queue.append((x, y))
        return dist[-1]


if __name__ == '__main__':
    print(Solution().minCost_2(
        [[3, 4, 3], [2, 2, 2], [2, 1, 1], [4, 3, 2], [2, 1, 4], [2, 4, 1], [3, 3, 3], [1, 4, 2], [2, 2, 1], [2, 1, 1],
         [3, 3, 1], [4, 1, 4], [2, 1, 4], [3, 2, 2], [3, 3, 1], [4, 4, 1], [1, 2, 2], [1, 1, 1], [1, 3, 4], [1, 2, 1],
         [2, 2, 4], [2, 1, 3], [1, 2, 1], [4, 3, 2], [3, 3, 4], [2, 2, 1], [3, 4, 3], [4, 2, 3], [4, 4, 4]]))
