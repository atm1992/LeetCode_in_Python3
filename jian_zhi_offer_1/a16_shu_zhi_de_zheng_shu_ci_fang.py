# -*- coding: UTF-8 -*-
"""
title: 数值的整数次方
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，x^n）。不得使用库函数，同时不需要考虑大数问题。


示例 1：
输入：x = 2.00000, n = 10
输出：1024.00000

示例 2：
输入：x = 2.10000, n = 3
输出：9.26100

示例 3：
输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25


提示：
-100.0 < x < 100.0
-2^31 <= n <= 2^31-1
-10^4 <= x^n <= 10^4
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """快速幂 + 递归"""

        def quick_mul(n: int) -> float:
            if n == 0:
                return 1.0
            y = quick_mul(n // 2)
            return y * y * x if n & 1 else y * y

        if x == 0:
            return 0
        res = quick_mul(abs(n))
        return res if n >= 0 else 1.0 / res

    def myPow_2(self, x: float, n: int) -> float:
        """迭代"""
        if x == 0:
            return 0
        res = 1.0
        if n < 0:
            x, n = 1.0 / x, -n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res


if __name__ == '__main__':
    print(Solution().myPow_2(20, -2))
