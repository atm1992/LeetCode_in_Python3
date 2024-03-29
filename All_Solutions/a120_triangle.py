# -*- coding: UTF-8 -*-
"""
title: 三角形最小路径和
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.


Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10


Constraints:
1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-10^4 <= triangle[i][j] <= 10^4

Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
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
    print(Solution().minimumTotal_2(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
