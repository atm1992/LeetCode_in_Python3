# -*- coding: utf-8 -*-
# @date: 2023/4/2
# @author: liuquan
"""
title: 多边形三角剖分的最低得分
You have a convex n-sided polygon where each vertex has an integer value. You are given an integer array values where values[i] is the value of the ith vertex (i.e., clockwise order).
You will triangulate the polygon into n - 2 triangles. For each triangle, the value of that triangle is the product of the values of its vertices, and the total score of the triangulation is the sum of these values over all n - 2 triangles in the triangulation.
Return the smallest possible total score that you can achieve with some triangulation of the polygon.


Example 1:
Input: values = [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.

Example 2:
Input: values = [3,7,4,5]
Output: 144
Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.
The minimum score is 144.

Example 3:
Input: values = [1,3,1,4,1,5]
Output: 13
Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.


Constraints:
n == values.length
3 <= n <= 50
1 <= values[i] <= 100
"""
import sys
from functools import lru_cache
from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        """
        动态规划。
        dp[i][j] 表示i、i+1、……、j-1、j这些顶点构成的凸多边形进行三角剖分后的最低得分。j >= i + 2
        假设存在一个顶点k (i < k < j)，使得 i、k、j 这3个顶点构成一个三角形。该三角形将原来的凸多边形划分为至多3个部分
        状态转移方程：
        1、顶点 i、i+1、……、k-1、k 构成的凸多边形，最低得分为dp[i][k]。当 k == i+1 时，这部分不存在，得分为0
        2、顶点 i、k、j 构成的三角形。得分为 values[i] * values[k] * values[j]
        3、顶点 k、k+1、……、j-1、j 构成的凸多边形，最低得分为dp[k][j]。当 k == j-1 时，这部分不存在，得分为0
        综上，dp[i][j] = min(dp[i][k] + values[i] * values[k] * values[j] + dp[k][j])
        最终返回结果为dp[0][n-1]，代码实现上可使用记忆化搜索
        """

        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            if j < i + 2:
                return 0
            if j == i + 2:
                return values[i] * values[i + 1] * values[j]
            return min(dfs(i, k) + values[i] * values[k] * values[j] + dfs(k, j) for k in range(i + 1, j))

        return dfs(0, len(values) - 1)

    def minScoreTriangulation_2(self, values: List[int]) -> int:
        """将方法一翻译成迭代形式"""
        MAX_INT = sys.maxsize
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                res = MAX_INT
                for k in range(i + 1, j):
                    res = min(res, dp[i][k] + values[i] * values[k] * values[j] + dp[k][j])
                dp[i][j] = res
        return dp[0][n - 1]


if __name__ == '__main__':
    print(Solution().minScoreTriangulation(values=[3, 7, 4, 5]))
