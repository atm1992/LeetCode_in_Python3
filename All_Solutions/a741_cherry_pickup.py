# -*- coding: UTF-8 -*-
"""
title: 摘樱桃
You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.
    0 means the cell is empty, so you can pass through,
    1 means the cell contains a cherry that you can pick up and pass through, or
    -1 means the cell contains a thorn that blocks your way.
Return the maximum number of cherries you can collect by following the rules below:
    Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with value 0 or 1).
    After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.
    When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
    If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.


Example 1:
Input: grid = [[0,1,-1],[1,0,-1],[1,1,1]]
Output: 5
Explanation: The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.

Example 2:
Input: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
Output: 0


Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 50
grid[i][j] is -1, 0, or 1.
grid[0][0] != -1
grid[n - 1][n - 1] != -1
"""
from functools import lru_cache
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        动态规划
        从(n-1, n-1)到(0, 0)这条路径可以等价的看作从(0, 0)到(n-1, n-1)。可以认为有两个人同时从(0, 0)到(n-1, n-1)，最终结果为这两个人摘樱桃个数之和的最大值。
        因为两个人同时都从(0, 0)出发，并且每次都是走一步(速度相同)，所以在相同时间的情况下，他们向下走的步数与向右走的步数之和肯定是相同的，假设为k，即 i1 + j1 = i2 + j2 = k
        因此，若 i1 == i2，则必然有 j1 == j2，即 这两个人走到了同一个格子。
        dp[k][i1][i2] 表示两个人(设为A和B)都走了k步的情况下(此时A在(i1, k - i1)、B在(i2, k - i2))，摘樱桃个数之和的最大值。
        状态转移方程：
        1、若从k-1步走到k步时，A和B都是向下走的，则表示从 dp[k-1][i1-1][i2-1] 转移而来
        2、若从k-1步走到k步时，A和B都是向右走的，则表示从 dp[k-1][i1][i2] 转移而来
        3、若从k-1步走到k步时，A是向下走的，而B是向右走的，则表示从 dp[k-1][i1-1][i2] 转移而来
        4、若从k-1步走到k步时，A是向右走的，而B是向下走的，则表示从 dp[k-1][i1][i2-1] 转移而来
        以上4种情况取最大值，然后加上 grid[i1][k - i1] 和 grid[i2][k - i2]。注意：若i1 == i2，则只需加上其中一个就行。
        边界条件：k=0时，表示A和B都位于起点(0, 0)，此时摘樱桃个数为grid[0][0]，即 dp[0][0][0] = grid[0][0]
        减少循环次数：
        根据观察其实可以发现，(i1, j1)、(i2, j2)的连线，始终与副对角线平行。为减少不必要的重复计算，可以让A走副对角线的右上半部分，而B走副对角线的左下半部分。
        这样一来，始终满足 i1 <= i2, 即 j1 >= j2
        """
        n = len(grid)
        # i1、i2的取值范围都是 [0, n-1]，步数的取值范围为 [0, 2*n - 2]，因为要么向下走、要么向右走。
        dp = [[[float('-inf')] * n for _ in range(n)] for _ in range(2 * n - 1)]
        dp[0][0][0] = grid[0][0]
        for k in range(1, 2 * n - 1):
            # 当k <= n-1时，i1的取值范围：[0, k+1)；当k > n-1时，i1的取值范围：[k-n+1, n)。
            for i1 in range(max(k - n + 1, 0), min(k + 1, n)):
                if grid[i1][k - i1] == -1:
                    continue
                # 始终满足 i1 <= i2。另外，为保证j2 >= 0，当k <= n-1时，i2最大为k
                for i2 in range(i1, min(k + 1, n)):
                    if grid[i2][k - i2] == -1:
                        continue
                    # 从k-1步走到k步时，A和B都是向右走的
                    pre = dp[k - 1][i1][i2]
                    if i1 > 0 and i2 > 0:
                        # 从k-1步走到k步时，A和B都是向下走的
                        pre = max(pre, dp[k - 1][i1 - 1][i2 - 1])
                    # 注意：这里不要写成 elif，因为我们要的是取这4种情况的最大值
                    if i1 > 0:
                        # 从k-1步走到k步时，A是向下走的，而B是向右走的
                        pre = max(pre, dp[k - 1][i1 - 1][i2])
                    if i2 > 0:
                        # 从k-1步走到k步时，A是向右走的，而B是向下走的
                        pre = max(pre, dp[k - 1][i1][i2 - 1])
                    pre += grid[i1][k - i1]
                    if i1 != i2:
                        pre += grid[i2][k - i2]
                    dp[k][i1][i2] = pre
        # 若从(0, 0)到(n-1, n-1)不存在一条可行的路径，则返回0，此时的dp[-1][-1][-1]为float('-inf')
        return int(max(dp[-1][-1][-1], 0))

    def cherryPickup_2(self, grid: List[List[int]]) -> int:
        """
        DFS + 记忆化
        """

        @lru_cache(maxsize=None)
        def dfs(i1: int, j1: int, i2: int, j2: int) -> float:
            if not 0 <= i1 < n or not 0 <= j1 < n or not 0 <= i2 < n or not 0 <= j2 < n:
                return float('-inf')
            if grid[i1][j1] == -1 or grid[i2][j2] == -1:
                return float('-inf')
            if i1 == n - 1 and j1 == n - 1:
                return grid[i1][j1]
            res = max(dfs(i1 + 1, j1, i2 + 1, j2), dfs(i1 + 1, j1, i2, j2 + 1), dfs(i1, j1 + 1, i2 + 1, j2), dfs(i1, j1 + 1, i2, j2 + 1))
            res += grid[i1][j1]
            if i1 != i2 and j1 != j2:
                res += grid[i2][j2]
            return res

        n = len(grid)
        return int(max(dfs(0, 0, 0, 0), 0))


if __name__ == '__main__':
    print(Solution().cherryPickup_2([[0, 1, -1], [1, 0, -1], [1, 1, 1]]))
