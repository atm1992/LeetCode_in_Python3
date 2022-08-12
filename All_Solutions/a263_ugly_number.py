# -*- coding: UTF-8 -*-
"""
title: 丑数
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return true if n is an ugly number.


Example 1:
Input: n = 6
Output: true
Explanation: 6 = 2 × 3

Example 2:
Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Example 3:
Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.


Constraints:
-2^31 <= n <= 2^31 - 1
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        """丑数n可写做 2^a + 3^b + 5^c 的形式，a、b、c均为非负整数，当a、b、c均为0时，n == 1。
        可以对n反复除以2、3、5，直到n等于1，则表示n为丑数。若n最终不为1，则表示n包含其它质因数，不是丑数。"""
        # 1是第一个丑数，丑数要求是正整数
        if n < 1:
            return False
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        return n == 1
