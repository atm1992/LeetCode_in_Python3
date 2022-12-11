# -*- coding: UTF-8 -*-
"""
title: 雇佣 K 名工人的最低成本
There are n workers. You are given two integer arrays quality and wage where quality[i] is the quality of the ith worker and wage[i] is the minimum wage expectation for the ith worker.
We want to hire exactly k workers to form a paid group. To hire a group of k workers, we must pay them according to the following rules:
    Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
    Every worker in the paid group must be paid at least their minimum wage expectation.
Given the integer k, return the least amount of money needed to form a paid group satisfying the above conditions. Answers within 10^-5 of the actual answer will be accepted.


Example 1:
Input: quality = [10,20,5], wage = [70,50,30], k = 2
Output: 105.00000
Explanation: We pay 70 to 0th worker and 35 to 2nd worker.

Example 2:
Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
Output: 30.66667
Explanation: We pay 4 to 0th worker, 13.33333 to 2nd and 3rd workers separately.


Constraints:
n == quality.length == wage.length
1 <= k <= n <= 10^4
1 <= quality[i], wage[i] <= 10^4
"""
import heapq
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        """
        贪心 + 优先队列(最大堆)
        假设有一个k名工人组成的工资组，这k名工人的总质量为total_q，总成本为total_c。其中第i名工人的质量为quality[i]，最低期望工资为wage[i]。
        根据题目要求，对于任意一名工人，都要满足条件：total_c * quality[i] / total_q >= wage[i]，即 total_c >= total_q * wage[i] / quality[i]
        对于总质量均为total_q的多个工资组，工资组中最大的wage[i] / quality[i]越小，总成本total_c也就越小。因此可以按 wage[i] / quality[i] 升序
        同时，工资组的total_q越小，total_c也会越小，可以使用优先队列(最大堆)来维护质量最小的k-1名工人，遍历时，将当前工人与质量最小的k-1名工人组成工资组，
        然后计算当前工资组的总成本，比较并更新当前res。
        """
        res = float('inf')
        # 按 wage[i] / quality[i] 升序
        pairs = sorted(zip(quality, wage), key=lambda pair: pair[1] / pair[0])
        queue, total_q = [], 0
        for i, (q, w) in enumerate(pairs):
            # queue 用于记录当前质量最小的k-1名工人
            heapq.heappush(queue, -q)
            total_q += q
            if i >= k - 1:
                # 当前工人的 w / q 是整个工资组中最大的，因为pairs已按 w / q 升序
                res = min(res, total_q * w / q)
                # 减去质量最大的那名工人，使queue中维持k-1名质量最小的工人。因为queue中的质量值是保存的负数，所以是 +=
                # 随着继续向后遍历pairs，工资组中最大的w / q会越来越大，所以此时为了获得总的最低成本，total_q需要尽可能小。
                # 注意：pairs是按 w / q 升序的，w / q小，不表示q也小，所以向后遍历pairs的过程中，total_q是有可能变小的
                total_q += heapq.heappop(queue)
        return round(res, 5)


if __name__ == '__main__':
    print(Solution().mincostToHireWorkers(quality=[3, 1, 10, 10, 1], wage=[4, 8, 2, 2, 7], k=3))
