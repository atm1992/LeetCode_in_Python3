# -*- coding: UTF-8 -*-
"""
title: 不同路径
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?


Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:
Input: m = 7, n = 3
Output: 28

Example 4:
Input: m = 3, n = 3
Output: 6


Constraints:
1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10^9.
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        动态规划
        dp[i][j] 表示从(0, 0)走到(i, j)的路径数量。因为只能向下或向右移动，所以dp[i][j]只可能从dp[i-1][j]或dp[i][j-1]转移而来
        状态转移方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]
        初始值：dp[0][0] = 1
        利用滚动数组的思想，降低空间复杂度
        """
        dp = [1] + [0] * (n - 1)
        for i in range(m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]

    def uniquePaths_2(self, m: int, n: int) -> int:
        """
        组合数学
        从m+n-2个元素中选出m-1个元素的组合个数
        """
        if m < n:
            return self.uniquePaths_2(n, m)
        a = b = 1
        for i in range(1, n):
            a *= i
            b *= i + m - 1
        return b // a


if __name__ == '__main__':
    print(Solution().uniquePaths_2(m=3, n=7))
