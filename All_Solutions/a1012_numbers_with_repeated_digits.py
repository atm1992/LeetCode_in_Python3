# -*- coding: UTF-8 -*-
"""
title: 至少有 1 位重复的数字
Given an integer n, return the number of positive integers in the range [1, n] that have at least one repeated digit.


Example 1:
Input: n = 20
Output: 1
Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.

Example 2:
Input: n = 100
Output: 10
Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.

Example 3:
Input: n = 1000
Output: 262


Constraints:
1 <= n <= 10^9
"""
from functools import lru_cache


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        """
        状态压缩 + 记忆化搜索。
        逆向思维，首先求出[0, n]范围内没有重复数字的正整数个数total，然后最终结果等于 n - total + 1。因为total中包含了0，所以多减了一个
        """
        digits = list(map(int, str(n)))
        size = len(digits)

        @lru_cache(None)
        def dfs(i: int, tight: bool, mask: int) -> int:
            if i == size:
                return 1
            upper_limit = digits[i] if tight else 9
            total = 0
            for d in range(upper_limit + 1):
                if mask & (1 << d):
                    continue
                nxt_tight = tight and d == upper_limit
                nxt_mask = mask if mask == 0 and d == 0 else mask | (1 << d)
                total += dfs(i + 1, nxt_tight, nxt_mask)
            return total

        return n - dfs(0, True, 0) + 1


if __name__ == '__main__':
    print(Solution().numDupDigitsAtMostN(1000))
