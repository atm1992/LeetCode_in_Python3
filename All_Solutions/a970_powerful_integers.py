# -*- coding: utf-8 -*-
# @date: 2023/5/2
# @author: liuquan
"""
title: 强整数
Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to bound.
An integer is powerful if it can be represented as x^i + y^j for some integers i >= 0 and j >= 0.
You may return the answer in any order. In your answer, each value should occur at most once.


Example 1:
Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation:
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2

Example 2:
Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]


Constraints:
1 <= x, y <= 100
0 <= bound <= 10^6
"""
from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        """
        哈希表 + 枚举
        由于 bound <= 10^6 < 1024 * 1024 = 2^20
        1、若 x = 1，则无论i为多少，x^i始终等于1
        2、若 x > 1，则 i < 20
        """
        res = set()
        a = 1
        for i in range(20):
            b = 1
            for j in range(20):
                if a + b <= bound:
                    res.add(a + b)
                if y == 1:
                    break
                b *= y
            if x == 1:
                break
            a *= x
        return list(res)


if __name__ == '__main__':
    print(Solution().powerfulIntegers(x=2, y=3, bound=10))
