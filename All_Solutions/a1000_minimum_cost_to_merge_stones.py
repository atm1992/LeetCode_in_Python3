# -*- coding: utf-8 -*-
# @date: 2023/4/4
# @author: liuquan
"""
title: 合并石头的最低成本
There are n piles of stones arranged in a row. The ith pile has stones[i] stones.
A move consists of merging exactly k consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these k piles.
Return the minimum cost to merge all piles of stones into one pile. If it is impossible, return -1.


Example 1:
Input: stones = [3,2,4,1], k = 2
Output: 20
Explanation: We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.

Example 2:
Input: stones = [3,2,4,1], k = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.

Example 3:
Input: stones = [3,5,1,2,6], k = 3
Output: 25
Explanation: We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.


Constraints:
n == stones.length
1 <= n <= 30
1 <= stones[i] <= 100
2 <= k <= 30
"""
import sys
from typing import List


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        """
        动态规划(区间DP) + 前缀和
        因为最终要把所有石头都合并为1堆，所以最后一步操作就是将k堆石头合并为1堆，而这最后一步的成本固定为 sum(stones)
        因此原问题转化为求解将所有石头合并为k堆的最低成本，此时可将所有石头划分为左右两个部分，左边合并为1堆，右边合并为k-1堆
        dp[i][j][m] 表示将区间[i, j]内的石头合并为m堆的最低成本
        dp[i][j][m] = min(dp[i][p][1] + dp[p+1][j][m-1])，其中 i <= p < j，2 <= m <= k
        注意：分界点p虽然可以从i逐个加1到j-1，但其中会有很多无用计算，因为要将区间[i, p]合并为1堆，区间长度n必须满足 (n - 1) % (k - 1) == 0
        即 要求 (p - i + 1 - 1) % (k - 1) == 0，因此分界点p的取值为：i、i + (k - 1) * 1、i + (k - 1) * 2、……
        """
        MAX_INT = sys.maxsize
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1
        dp = [[[MAX_INT] * (k + 1) for _ in range(n)] for _ in range(n)]
        # 前缀和数组。为了方便之后计算子数组的和
        pre_sum = [0]
        for i in range(n):
            # 将1堆石头合并为1堆的成本为0，因为无需操作
            dp[i][i][1] = 0
            pre_sum.append(pre_sum[-1] + stones[i])
        # 问题从小递推到大，先两个两个石头考虑，再三个三个石头考虑，通过size来控制区间[i, j]内的石头数量
        for size in range(2, n + 1):
            for i in range(n - size + 1):
                j = i + size - 1
                # 将区间[i, j]内的石头合并为 2堆 ~ k堆
                for m in range(2, k + 1):
                    for p in range(i, j, k - 1):
                        dp[i][j][m] = min(dp[i][j][m], dp[i][p][1] + dp[p + 1][j][m - 1])
                dp[i][j][1] = dp[i][j][k] + pre_sum[j + 1] - pre_sum[i]
        return dp[0][n - 1][1]

    def mergeStones_2(self, stones: List[int], k: int) -> int:
        """
        优化方法一
        对于区间[i, j]内的石头，最终一定是合并到小于k堆的状态，只有当(j - i) % (k - 1) == 0时，才能合并为1堆，其余情况只能合并到 2 ~ k-1 堆
        dp[i][j] 表示将区间[i, j]内的石头合并到不能再合并时的最低成本，从而减少一个维度
        遍历完所有的分界点p：i、i + (k - 1) * 1、i + (k - 1) * 2、…… 就能得到最小的dp[i][j]，只不过此时的dp[i][j]不一定是dp[i][j][1]
        只有当(j - i) % (k - 1) == 0时，才需要计算dp[i][j][1]
        """
        MAX_INT = sys.maxsize
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1
        dp = [[MAX_INT] * n for _ in range(n)]
        pre_sum = [0]
        for i in range(n):
            dp[i][i] = 0
            pre_sum.append(pre_sum[-1] + stones[i])
        for size in range(2, n + 1):
            for i in range(n - size + 1):
                j = i + size - 1
                for p in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][p] + dp[p + 1][j])
                if (j - i) % (k - 1) == 0:
                    # 此时的dp[i][j]表示将区间[i, j]内的石头合并到1堆时的最低成本
                    dp[i][j] = dp[i][j] + pre_sum[j + 1] - pre_sum[i]
        return dp[0][n - 1]


if __name__ == '__main__':
    print(Solution().mergeStones_2(stones=[3, 5, 1, 2, 6], k=3))
