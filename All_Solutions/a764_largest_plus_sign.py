# -*- coding: UTF-8 -*-
"""
title: 最大加号标志
You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices given in the array mines. The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.
Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.
An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1 going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.


Example 1:
Input: n = 5, mines = [[4,2]]
Output: 2
Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.

Example 2:
Input: n = 1, mines = [[0,0]]
Output: 0
Explanation: There is no plus sign, so return 0.


Constraints:
1 <= n <= 500
1 <= mines.length <= 5000
0 <= xi, yi < n
All the pairs (xi, yi) are unique.
"""
from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        """动态规划"""
        # dp[i][j]表示以(i,j)为中心的最大加号标志的阶数，二维数组dp中的最大值即为最终结果
        # 每个点(i,j)的最大阶数等于up、down、left、right这4个方向上的1的个数的最小值，所以将每个点的初始值设为n
        dp = [[n] * n for _ in range(n)]
        for r, c in mines:
            dp[r][c] = 0
        # 可将i作为行，j、k均为列；还可将i作为列，j、k均为行
        for i in range(n):
            up = down = left = right = 0
            for j, k in zip(range(n), range(n - 1, -1, -1)):
                # left 从左往右统计每行中的1的个数。第0行 ——> 第n-1行
                left = left + 1 if dp[i][j] else 0
                dp[i][j] = min(dp[i][j], left)

                # right 从右往左统计每行中的1的个数。第0行 ——> 第n-1行
                right = right + 1 if dp[i][k] else 0
                dp[i][k] = min(dp[i][k], right)

                # up 从上往下统计每列中的1的个数。第0列 ——> 第n-1列
                up = up + 1 if dp[j][i] else 0
                dp[j][i] = min(dp[j][i], up)

                # down 从下往上统计每列中的1的个数。第0列 ——> 第n-1列
                down = down + 1 if dp[k][i] else 0
                dp[k][i] = min(dp[k][i], down)
        return max(max(row) for row in dp)


if __name__ == '__main__':
    print(Solution().orderOfLargestPlusSign(n=5, mines=[[4, 2]]))
