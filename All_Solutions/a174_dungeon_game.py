# -*- coding: UTF-8 -*-
"""
title: 地下城游戏
The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.
The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.
Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).
To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.
Return the knight's minimum initial health so that he can rescue the princess.
Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.


Example 1:
Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.

Example 2:
Input: dungeon = [[0]]
Output: 1


Constraints:
m == dungeon.length
n == dungeon[i].length
1 <= m, n <= 200
-1000 <= dungeon[i][j] <= 1000
"""
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
        动态规划。假设dp[i][j]为从点(i,j)到终点(m-1, n-1)所需的最小初始值，它可能从dp[i+1][j]和dp[i][j+1]转移而来，取他两的较小值即可。
        从终点(m-1, n-1)开始累加点数，若点数为-5，则在前一格的剩余点数需要为6；若点数为+5，则在前一格的剩余点数需要为1，因为如果在前一格的剩余点数为0的话，就挂了。
        由此可见，从后往前走的过程中，遇到的正点数，只能用来抵消已经遇到的负点数，而不能把它往前携带。只有负点数才能往前携带。
        二维dp数组为 m+1 * n+1，初始值均为很大的正数，因为是从终点(m-1, n-1)开始计算，所以把点(m, n-1)和点(m-1, n)的初始值置为1，
        因为到达终点(m-1, n-1)时，剩余的点数至少需要为1，即 min(dp[m][n-1], dp[m-1][n]) = 1，然后再 - dungeon[m-1][n-1] ，得出到达终点(m-1, n-1)所需的点数，
        若dungeon[m-1][n-1]为正数，则表示所需点数只需为最小值1。
        可以使用滚动数组来优化空间复杂度，因为每次循环过程中，只用到了最后两行。
        """
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[m][n - 1] = dp[m - 1][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # dp[i][j] 始终是一个大于等于1的正数，当dungeon[i][j]是一个负数时，通过减号变成正数，从而进一步增大dp[i][j]，表示进入点(i, j)所需的初始值越大。
                # 若dungeon[i][j]是一个正数，则表示到达点(i, j)时，可以提供血包，用来抵消之前遇到的负点数，从而使dp[i][j]减小，不过，dp[i][j]再小也不能小于1，
                # 因为进入任何一个点，点数都至少需要为1，否则它在进入该点之前，就已经挂了
                # 当min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j] 小于1时，则表示所需点数只需为最小值1
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)
        return int(dp[0][0])


if __name__ == '__main__':
    print(Solution().calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
