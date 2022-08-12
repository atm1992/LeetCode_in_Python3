# -*- coding: UTF-8 -*-
"""
title: 因子的组合
Numbers can be regarded as the product of their factors.
    For example, 8 = 2 x 2 x 2 = 2 x 4.
Given an integer n, return all possible combinations of its factors. You may return the answer in any order.
Note that the factors should be in the range [2, n - 1].


Example 1:
Input: n = 1
Output: []

Example 2:
Input: n = 12
Output: [[2,6],[3,4],[2,2,3]]

Example 3:
Input: n = 37
Output: []


Constraints:
1 <= n <= 10^7
"""
from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        """回溯"""

        def dfs(num: int, start: int) -> List[List[int]]:
            res = []
            # 从start开始拆分num
            for factor in range(start, int(num ** 0.5) + 1):
                if num % factor == 0:
                    res.append([factor, num // factor])
                    # 从当前factor开始，继续拆分num // factor。从而保证每个组合中的factor都是递增的，因此实现了去重
                    for sub_res in dfs(num // factor, factor):
                        res.append([factor] + sub_res)
            return res

        return dfs(n, 2)


if __name__ == '__main__':
    print(Solution().getFactors(12))
