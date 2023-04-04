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
        """回溯。超时，通过 29/84 个测试用例"""
        n = len(stones)
        # 原本就只有一堆石头的话，就不用合并了
        if n == 1:
            return 0
        if n < k or (len(stones) - k) % (k - 1) != 0:
            return -1

        def dfs(nums: List[int]) -> int:
            n = len(nums)
            if n == k:
                return sum(nums)
            res = sys.maxsize
            for i in range(n - k + 1):
                cur = sum(nums[i:i + k])
                res = min(res, cur + dfs(nums[:i] + [cur] + nums[i + k:]))
            return res

        return dfs(stones)


if __name__ == '__main__':
    print(Solution().mergeStones(stones=[3, 5, 1, 2, 6], k=3))
