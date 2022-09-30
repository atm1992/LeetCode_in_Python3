# -*- coding: UTF-8 -*-
"""
title: 出界的路径数
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.
Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 10^9 + 7.


Example 1:
Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

Example 2:
Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12


Constraints:
1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n
"""


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """
        动态规划
        假设 dp[k][i][j] 表示移动k次后到达坐标(i, j)的路径数量
        状态转移方程：
        假设从坐标(i, j)移动到的下一个坐标为(i', j')，(i', j')的可取值为：(i-1, j), (i+1, j), (i, j-1), (i, j+1)
        若(i', j')未出界，则 dp[k+1][i'][j'] += dp[k][i][j]
        若(i', j')出界了，则 出界的路径数res += dp[k][i][j]
        边界条件：
        当k为0时，dp[0][startRow][startColumn] = 1, dp[0][i][j] = 0，(i, j) != (startRow, startColumn)
        """
        mod = 10 ** 9 + 7
        res = 0
        dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
        dp[0][startRow][startColumn] = 1
        for k in range(maxMove):
            for i in range(m):
                for j in range(n):
                    if dp[k][i][j] > 0:
                        for nxt_i, nxt_j in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                            if 0 <= nxt_i < m and 0 <= nxt_j < n:
                                dp[k + 1][nxt_i][nxt_j] = (dp[k + 1][nxt_i][nxt_j] + dp[k][i][j]) % mod
                            else:
                                res = (res + dp[k][i][j]) % mod
        return res


if __name__ == '__main__':
    print(Solution().findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1))
