# -*- coding: UTF-8 -*-
"""
title: 第 k 个数
Design an algorithm to find the kth number such that the only prime factors are 3, 5, and 7. Note that 3, 5, and 7 do not have to be factors, but it should not have any other prime factors. For example, the first several multiples would be (in order) 1, 3, 5, 7, 9, 15, 21.


Example 1:
Input: k = 5
Output: 9
"""
import heapq


class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        """优先队列"""
        queue = [1]
        for _ in range(k - 1):
            cur = heapq.heappop(queue)
            heapq.heappush(queue, cur * 3)
            heapq.heappush(queue, cur * 5)
            heapq.heappush(queue, cur * 7)
            while queue[0] == cur:
                heapq.heappop(queue)
        return queue[0]

    def getKthMagicNumber_2(self, k: int) -> int:
        """动态规划 + 三指针"""
        dp = [1]
        p3 = p5 = p7 = 0
        for _ in range(k - 1):
            n3, n5, n7 = dp[p3] * 3, dp[p5] * 5, dp[p7] * 7
            cur = min(n3, n5, n7)
            if n3 == cur:
                p3 += 1
            if n5 == cur:
                p5 += 1
            if n7 == cur:
                p7 += 1
            dp.append(cur)
        return dp[-1]


if __name__ == '__main__':
    print(Solution().getKthMagicNumber_2(5))
