# -*- coding: UTF-8 -*-
"""
title: 石子游戏 II
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 
Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
The game continues until all the stones have been taken.
Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.


Example 1:
Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger.

Example 2:
Input: piles = [1,2,3,4,5,100]
Output: 104


Constraints:
1 <= piles.length <= 100
1 <= piles[i] <= 10^4
"""
from functools import lru_cache
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        """
        DFS + 记忆化。博弈
        因为两个人都发挥出最佳水平，所以要想让自己得到最多的石头，就要想办法让对方得到尽量少的石头，石头的总数量是固定的
        1、若Alice能一次性拿完所有的剩余石头，则直接结束游戏；
        2、若Alice不能一次性拿完，则Alice能拿到的石头 = 剩余的石头总量 - Bob所能拿到最少的石头
        """
        n = len(piles)
        # 后缀和数组
        suf_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf_sum[i] = suf_sum[i + 1] + piles[i]

        @lru_cache(maxsize=None)
        def dfs(i: int, M: int) -> int:
            """
            从piles[i]开始拿，最多能拿到的石头数量。M含义同题意，每次可以拿的堆数范围：1 <= X <= 2M
            """
            if i + 2 * M >= n:
                # 一次性拿完所有的剩余石头
                return suf_sum[i]
            bob_min_stones = suf_sum[0]
            # 假设Alice此次拿了1堆，拿了2堆，……，拿了2 * M堆。看看Alice此次拿多少堆，可以让Bob拿到最少的石头
            for x in range(1, 2 * M + 1):
                bob_min_stones = min(bob_min_stones, dfs(i + x, max(M, x)))
            return suf_sum[i] - bob_min_stones

        return dfs(0, 1)


if __name__ == '__main__':
    print(Solution().stoneGameII(piles=[1, 2, 3, 4, 5, 100]))
