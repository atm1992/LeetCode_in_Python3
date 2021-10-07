# -*- coding: UTF-8 -*-
"""
title:  Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:
-100.0 < x < 100.0
-2^31 <= n <= 2^31-1
-10^4 <= xn <= 10^4
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """快速幂 + 递归"""

        def quick_mul(N: int):
            if N == 0:
                return 1.0
            y = quick_mul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quick_mul(n) if n >= 0 else 1.0 / quick_mul(-n)

    def myPow_2(self, x: float, n: int) -> float:
        """快速幂 + 迭代。
        假设n=5，因为5 = 0b101 = 2^2 + 2^0，二进制位中那两个1的下标分别为2和0，所以x^5 = x^(2^2 + 2^0) = x^2^2 * x^2^0"""

        def quick_mul(N: int):
            res = 1.0
            factor = x
            while N > 0:
                # 二进制最低位为1
                if N % 2 == 1:
                    res *= factor
                # 无论二进制最低位是否为1，二进制低位每次向高位前进一步，都是在原来的基础上翻倍。然而只有在当前二进制位为1时，才会把值乘入结果
                factor *= factor
                N //= 2
            return res

        return quick_mul(n) if n >= 0 else 1.0 / quick_mul(-n)
