# -*- coding: UTF-8 -*-
"""
title: 路径的数目
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？


示例 1：
输入：m = 3, n = 7
输出：28

示例 2：
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下

示例 3：
输入：m = 7, n = 3
输出：28

示例 4：
输入：m = 3, n = 3
输出：6


提示：
1 <= m, n <= 100
题目数据保证答案小于等于 2 * 10^9
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
    print(Solution().uniquePaths(m=3, n=3))
