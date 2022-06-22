# -*- coding: UTF-8 -*-
"""
title: 三角形中最小路径之和
给定一个三角形 triangle ，找出自顶向下的最小路径和。
每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。


示例 1：
输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

示例 2：
输入：triangle = [[-10]]
输出：-10


提示：
1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-10^4 <= triangle[i][j] <= 10^4

进阶：
你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？
"""
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        动态规划
        dp[i][j] 表示从(0, 0)到(i, j)的最小路径之和
        状态转移方程：dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        通过逆序遍历j的方式来降低空间复杂度
        """
        # 三角形的总行数 等于 最后一行的列数
        n = len(triangle)
        dp = [0] * n
        for i in range(n):
            # 每一行的列数等于所在的行数(行数从1开始)
            for j in range(i, -1, -1):
                if i > 0:
                    if 0 < j < i:
                        dp[j] = min(dp[j - 1], dp[j]) + triangle[i][j]
                    elif j == i:
                        dp[j] = dp[j - 1] + triangle[i][j]
                    else:
                        dp[j] = dp[j] + triangle[i][j]
                # i == 0时，j一定为0
                else:
                    dp[j] = triangle[i][j]
        return min(dp)

    def minimumTotal_2(self, triangle: List[List[int]]) -> int:
        """动态规划。从三角形的底部开始转移，到顶部结束。最后直接返回dp[0]，而无需查找最小值"""
        # dp数组初始化为三角形的最后一行
        dp = triangle[-1][:]
        # 从倒数第二行开始向上转移
        for i in range(len(triangle) - 2, -1, -1):
            # 这里必须是正序遍历
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]


if __name__ == '__main__':
    print(Solution().minimumTotal_2([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
