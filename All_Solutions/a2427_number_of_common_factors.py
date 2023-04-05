# -*- coding: utf-8 -*-
# @date: 2023/4/5
# @author: liuquan
"""
title: 公因子的数目
Given two positive integers a and b, return the number of common factors of a and b.
An integer x is a common factor of a and b if x divides both a and b.


Example 1:
Input: a = 12, b = 6
Output: 4
Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.

Example 2:
Input: a = 25, b = 30
Output: 2
Explanation: The common factors of 25 and 30 are 1, 5.


Constraints:
1 <= a, b <= 1000
"""
from math import gcd


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        """枚举到最大公约数"""
        g = gcd(a, b)
        return sum(g % x == 0 for x in range(1, g + 1))

    def commonFactors_2(self, a: int, b: int) -> int:
        """优化枚举到最大公约数"""
        g = gcd(a, b)
        res, x = 0, 1
        while x * x <= g:
            if g % x == 0:
                res += 1
                if x * x < g:
                    res += 1
            x += 1
        return res


if __name__ == '__main__':
    print(Solution().commonFactors(a=25, b=30))
