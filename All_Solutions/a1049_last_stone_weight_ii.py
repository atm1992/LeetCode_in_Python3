# -*- coding: UTF-8 -*-
"""
title: 最后一块石头的重量 II
You are given an array of integers stones where stones[i] is the weight of the ith stone.
We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:
    If x == y, both stones are destroyed, and
    If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.
Return the smallest possible weight of the left stone. If there are no stones left, return 0.


Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.

Example 2:
Input: stones = [31,26,33,21,40]
Output: 5


Constraints:
1 <= stones.length <= 30
1 <= stones[i] <= 100
"""
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        动态规划 - 背包问题
        可以证明，无论按哪种顺序粉碎石头，最后一块石头的重量(若最后没有剩下石头，则认为最后一块石头的重量为0)总是可以表示成：
        将stones划分成重量相近的两堆石头，一堆的重量为neg，另一堆的重量为sum - neg，最终结果diff = sum - 2 * neg。
        要使最终的diff尽可能小，则需要使neg在不超过 sum//2 的前提下，尽可能大。
        因此原问题转化为0-1背包最值问题，从stones中选一堆石头放进最大容量为 sum//2 的背包，求能放进去的最大重量。
        dp[i][j] 表示在总重量不超过 j 的前提下，从前 i 块石头中能选取到的最大重量
        状态转移方程：dp[i][j] = max(dp[i-1][j - stones[i]] + stones[i])
        边界条件：从前 0 块石头中能选取到的最大重量为0，即 dp[0][*] = 0
        由状态转移方程可知，dp[i] 仅与 dp[i-1] 有关，所以可使用滚动数组的方式来降低空间复杂度
        """
        total = sum(stones)
        target = total // 2
        dp = [0] * (target + 1)
        for stone in stones:
            # 从 dp[i][target] 更新到 dp[i][stone]，dp[i][0] ~ dp[i][stone-1]无需计算，因为当前stone无法被使用，所以等于 dp[i-1][0] ~ dp[i-1][stone-1]
            for j in range(target, stone - 1, -1):
                # dp[i][j] = max(dp[i][j], dp[i-1][j - stone] + stone)
                dp[j] = max(dp[j], dp[j - stone] + stone)
        return total - 2 * dp[-1]


if __name__ == '__main__':
    print(Solution().lastStoneWeightII([31, 26, 33, 21, 40]))
