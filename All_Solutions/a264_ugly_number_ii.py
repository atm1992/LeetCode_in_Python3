# -*- coding: UTF-8 -*-
"""
title: 丑数 II
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the nth ugly number.


Example 1:
Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:
Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.


Constraints:
1 <= n <= 1690
"""
import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """最小堆"""
        factors = [2, 3, 5]
        visited = {1}
        min_heap = [1]
        for _ in range(n - 1):
            cur = heapq.heappop(min_heap)
            for factor in factors:
                nxt = cur * factor
                # 避免重复加入到min_heap
                if nxt not in visited:
                    visited.add(nxt)
                    heapq.heappush(min_heap, nxt)
        return min_heap[0]

    def nthUglyNumber_2(self, n: int) -> int:
        """动态规划。dp[i]表示第i个丑数，dp[1]=1。后面的丑数一定是由前面的丑数乘以2，或乘以3，或乘以5得来"""
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1
        for i in range(2, n + 1):
            num_2, num_3, num_5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            min_num = min(num_2, num_3, num_5)
            dp[i] = min_num
            if min_num == num_2:
                p2 += 1
            # 注意：这里不能用elif …… else。min_num = 6时，6 = 3 * 2 = 2 * 3，此时的num_2 == num_3，p2、p3都需要加1。min_num = 10时同理
            if min_num == num_3:
                p3 += 1
            if min_num == num_5:
                p5 += 1
        return dp[-1]


if __name__ == '__main__':
    print(Solution().nthUglyNumber_2(10))
