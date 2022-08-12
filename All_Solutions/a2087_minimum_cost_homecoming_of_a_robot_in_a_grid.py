# -*- coding: UTF-8 -*-
"""
title: 网格图中机器人回家的最小代价
There is an m x n grid, where (0, 0) is the top-left cell and (m - 1, n - 1) is the bottom-right cell. You are given an integer array startPos where startPos = [startrow, startcol] indicates that initially, a robot is at the cell (startrow, startcol). You are also given an integer array homePos where homePos = [homerow, homecol] indicates that its home is at the cell (homerow, homecol).
The robot needs to go to its home. It can move one cell in four directions: left, right, up, or down, and it can not move outside the boundary. Every move incurs some cost. You are further given two 0-indexed integer arrays: rowCosts of length m and colCosts of length n.
    If the robot moves up or down into a cell whose row is r, then this move costs rowCosts[r].
    If the robot moves left or right into a cell whose column is c, then this move costs colCosts[c].
Return the minimum total cost for this robot to return home.


Example 1:
Input: startPos = [1, 0], homePos = [2, 3], rowCosts = [5, 4, 3], colCosts = [8, 2, 6, 7]
Output: 18
Explanation: One optimal path is that:
Starting from (1, 0)
-> It goes down to (2, 0). This move costs rowCosts[2] = 3.
-> It goes right to (2, 1). This move costs colCosts[1] = 2.
-> It goes right to (2, 2). This move costs colCosts[2] = 6.
-> It goes right to (2, 3). This move costs colCosts[3] = 7.
The total cost is 3 + 2 + 6 + 7 = 18

Example 2:
Input: startPos = [0, 0], homePos = [0, 0], rowCosts = [5], colCosts = [26]
Output: 0
Explanation: The robot is already at its home. Since no moves occur, the total cost is 0.


Constraints:
m == rowCosts.length
n == colCosts.length
1 <= m, n <= 10^5
0 <= rowCosts[r], colCosts[c] <= 10^4
startPos.length == 2
homePos.length == 2
0 <= startrow, homerow < m
0 <= startcol, homecol < n
"""
from typing import List


class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        """
        贪心。脑筋急转弯
        假设起点为(i, j)，终点为(x, y)。
        若 x > i and y > j，则从(i, j)到(x, y)的最小代价路径一定是最短路径，最短路径即 向下走 (x-i) 步，向右走 (y-j) 步。
        至于怎么走，先往右再往下，还是先往下再往右，对于最终要求的最小代价并没影响，(x-i) + (y-j) 步的代价是确定的。
        以 (i, j) ——> (i, k) 为例，(i, j) ——> (i, j+1) ——> …… ——> (i, k-1) ——> (i, k) 就是最小代价路径，也是最短路径；
        这条路径的代价一定小于等于其它非直接路径，例如：(i, j) ——> (i+1, j) ——> (i+1, j+1) ——> …… ——> (i+1, k-1) ——> (i, k-1) ——> (i, k)。
        因为0 <= rowCosts[r], colCosts[c]。
        综上，绕路的代价一定会大于等于直接路径的代价，因为绕路的代价 = 直接路径的代价 + 一些大于等于0的其它代价
        """
        res = 0
        s_i, s_j = startPos
        h_i, h_j = homePos
        if s_i <= h_i:
            for i in range(s_i + 1, h_i + 1):
                res += rowCosts[i]
        else:
            for i in range(h_i, s_i):
                res += rowCosts[i]
        if s_j <= h_j:
            for j in range(s_j + 1, h_j + 1):
                res += colCosts[j]
        else:
            for j in range(h_j, s_j):
                res += colCosts[j]
        return res


if __name__ == '__main__':
    print(Solution().minCost(startPos=[1, 0], homePos=[2, 3], rowCosts=[5, 4, 3], colCosts=[8, 2, 6, 7]))
