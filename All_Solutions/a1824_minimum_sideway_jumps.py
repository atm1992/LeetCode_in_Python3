# -*- coding: utf-8 -*-
# @date: 2023/3/30
# @author: liuquan
"""
title: 最少侧跳次数
There is a 3 lane road of length n that consists of n + 1 points labeled from 0 to n. A frog starts at point 0 in the second lane and wants to jump to point n. However, there could be obstacles along the way.
You are given an array obstacles of length n + 1 where each obstacles[i] (ranging from 0 to 3) describes an obstacle on the lane obstacles[i] at point i. If obstacles[i] == 0, there are no obstacles at point i. There will be at most one obstacle in the 3 lanes at each point.
    For example, if obstacles[2] == 1, then there is an obstacle on lane 1 at point 2.
The frog can only travel from point i to point i + 1 on the same lane if there is not an obstacle on the lane at point i + 1. To avoid obstacles, the frog can also perform a side jump to jump to another lane (even if they are not adjacent) at the same point if there is no obstacle on the new lane.
    For example, the frog can jump from lane 3 at point 3 to lane 1 at point 3.
Return the minimum number of side jumps the frog needs to reach any lane at point n starting from lane 2 at point 0.
Note: There will be no obstacles on points 0 and n.


Example 1:
Input: obstacles = [0,1,2,3,0]
Output: 2
Explanation: The optimal solution is shown by the arrows above. There are 2 side jumps (red arrows).
Note that the frog can jump over obstacles only when making side jumps (as shown at point 2).

Example 2:
Input: obstacles = [0,1,1,3,3,0]
Output: 0
Explanation: There are no obstacles on lane 2. No side jumps are required.

Example 3:
Input: obstacles = [0,2,1,0,3,0]
Output: 2
Explanation: The optimal solution is shown by the arrows above. There are 2 side jumps.


Constraints:
obstacles.length == n + 1
1 <= n <= 5 * 10^5
0 <= obstacles[i] <= 3
obstacles[0] == obstacles[n] == 0
"""
from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        """
        动态规划
        dp[i][j]表示到达点i的跑道j的最少侧跳次数。j的取值范围：[0, 2] 分别对应跑道1、跑道2、跑道3
        状态转移方程：
        1、若点i的跑道j处有障碍，则无法到达，因此将dp[i][j]取值为len(obstacles)，最少侧跳次数肯定小于该值
        2、若点i的跑道j处没有障碍，则可从dp[i-1][j]、dp[i][(j+1)%3]、dp[i][(j+2)%3]转移过来，
        注意：其它跑道要切换到跑道j，只能从dp[i]，而不是从dp[i-1]
        因此，需要先求出其它跑道的dp[i]，然后取最小值 + 1，更新dp[i][j]
        可使用滚动数组来优化空间复杂度
        """
        n = len(obstacles)
        # 初始时，在跑道2
        dp = [1, 0, 1]
        # 题目已告知点0和点n没有障碍
        for i in range(1, n):
            # 先只考虑同跑道，即 从dp[i-1][j]转移到dp[i][j]
            val = obstacles[i] - 1
            if val >= 0:
                dp[val] = n
            min_jumps = min(dp)
            for j in range(3):
                # 再考虑从其它跑道的dp[i]转移过来，只有当前跑道上没有障碍时，才能从其它跑道跳过来
                if j != val:
                    dp[j] = min(dp[j], min_jumps + 1)
        return min(dp)


if __name__ == '__main__':
    print(Solution().minSideJumps(obstacles=[0, 2, 1, 0, 3, 0]))
