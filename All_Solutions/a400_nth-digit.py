# -*- coding: UTF-8 -*-
"""
title: 第 N 位数字
Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].


Example 1:
Input: n = 3
Output: 3

Example 2:
Input: n = 11
Output: 0
Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.


Constraints:
1 <= n <= 2^31 - 1
"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        """
        二分查找 + 前缀和。
        1位数有：1 ~ 9，总共9个，位数之和为：1 * 9，1 表示每个数字只有1位。0单独考虑，n=0时，直接返回0
        2位数有：10 ~ 99，总共90个，位数之和为：2 * 90，2 表示每个数字有2位。
        3位数有：100 ~ 999，总共900个，位数之和为：3 * 900，3 表示每个数字有3位。
        以此类推 ……
        x位数有：10^(x-1) ~ 10^x - 1，总共10^x - 10^(x-1) = 9 * 10^(x-1)个，位数之和为：x * 9 * 10^(x-1)，x 表示每个数字有x位。
        由于 n < 2^31 = 2147483648 < 8100000000 = 9 * 9 * 10^8，即 x 最多为9
        """
        if n < 10:
            return n
        digit_pre_sum = [0] * 10
        for i in range(1, 10):
            digit_pre_sum[i] = i * 9 * (10 ** (i - 1)) + digit_pre_sum[i - 1]
        # n所在的整数，最少2位数，最多9位数
        left, right = 2, 9
        # 退出循环时，left == right，表示n所在的整数为left位数
        while left < right:
            mid = (left + right) // 2
            if digit_pre_sum[mid] < n:
                left = mid + 1
            else:
                right = mid
        # n所指位置在所有left位数中的下标，从0开始。0 ~ left-1位在第0个整数10 ** (left-1)中，left ~ 2*left-1位在第1个整数10 ** (left-1) + 1中
        idx = n - digit_pre_sum[left - 1] - 1
        start = 10 ** (left - 1)
        num = start + idx // left
        return int(str(num)[idx % left])

    def findNthDigit_2(self, n: int) -> int:
        """
        直接根据规律计算
        已知：x位数有9 * 10^(x-1)个，所有x位数的位数之和为：x * 9 * 10^(x-1)
        """
        # 其实当前方法能处理n为0的情况，不用这个判断也行
        if n < 10:
            return n
        # digit 表示当前遍历到的位数，初始时为1位数；
        # start 表示当前位数下的起始整数，1位数的起始整数为1
        # cnt 表示当前位数下的所有整数的位数之和，1位数的位数之和为9
        digit, start, cnt = 1, 1, 9
        while cnt < n:
            n -= cnt
            start *= 10
            digit += 1
            # 10 ** (digit - 1) == start
            cnt = digit * 9 * start
        # n所指位置在所有digit位数中的下标，从0开始
        idx = n - 1
        num = start + idx // digit
        # n = 0时，-1%1 = 0，int(str(0)[0]) = 0
        return int(str(num)[idx % digit])
