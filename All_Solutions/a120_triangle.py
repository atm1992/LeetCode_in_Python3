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
        """动态规划。假设从三角形顶部走到位置 (i,j) 的最小路径和为dp[i][j]，其中，i,j 均从0开始。第i行有i+1个元素
        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        特殊情况：
        一、j == 0 时，dp[i][0] = dp[i-1][0] + triangle[i][0]
        二、j == i 时，dp[i][i] = dp[i-1][i-1] + triangle[i][i]
        边界条件：dp[0][0] = triangle[0][0]
        最终，min(dp[i][0], ……, dp[i][i]) 便是从三角形顶部走到第i行的最小路径和。
        从状态转移方程可知，第i行的结果只会从第i-1行转换而来，因此可将dp数组从n*n压缩到2*n
        # 面试过程中，可询问面试官，是否可以直接修改原数组，这样就可以不使用额外空间。
        """
        n = len(triangle)
        dp = [[0] * n, [0] * n]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            cur, pre = i % 2, (i - 1) % 2
            dp[cur][0] = dp[pre][0] + triangle[i][0]
            for j in range(1, i):
                dp[cur][j] = min(dp[pre][j - 1], dp[pre][j]) + triangle[i][j]
            dp[cur][i] = dp[pre][i - 1] + triangle[i][i]
        return min(dp[(n - 1) % 2])

    def minimumTotal_2(self, triangle: List[List[int]]) -> int:
        """动态规划。进一步压缩dp数组，只需一个1*n的一维数组。依旧是从上往下计算，但对于每行，则是从后往前计算。"""
        n = len(triangle)
        dp = [0] * n
        dp[0] = triangle[0][0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                dp[j] = min(dp[j], dp[j - 1]) + triangle[i][j]
            dp[0] += triangle[i][0]
        return min(dp)

    def minimumTotal_3(self, triangle: List[List[int]]) -> int:
        """动态规划。从三角形的底部开始转移，到顶部结束。最后直接返回dp[0]，而无需查找最小值"""
        # dp数组初始化为三角形的最后一行
        dp = triangle[-1][:]
        # 从倒数第二行开始向上转移
        for i in range(len(triangle) - 2, -1, -1):
            # 这里必须从前往后计算
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]


if __name__ == '__main__':
    print(Solution().minimumTotal_3(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
