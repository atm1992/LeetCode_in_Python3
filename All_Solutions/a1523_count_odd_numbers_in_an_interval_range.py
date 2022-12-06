# -*- coding: UTF-8 -*-
"""
title: 在区间范围内统计奇数数目
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).


Example 1:
Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:
Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].


Constraints:
0 <= low <= high <= 10^9
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """暴力枚举。运行超时，通过 74/84 个测试用例"""
        res = 0
        for num in range(low, high + 1):
            res += num & 1
        return res

    def countOdds_2(self, low: int, high: int) -> int:
        """
        前缀和思想
        [0, n] 范围内的奇数个位为 (n+1) // 2，因为偶数个数要么等于奇数个数，要么比奇数个数多1
        """
        return (high + 1) // 2 - low // 2


if __name__ == '__main__':
    print(Solution().countOdds_2(3, 7))
