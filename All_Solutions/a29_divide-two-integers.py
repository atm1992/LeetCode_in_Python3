# -*- coding: UTF-8 -*-
"""
title: 两数相除
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, assume that your function returns 2^31 − 1 when the division result overflows.


Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

Example 3:
Input: dividend = 0, divisor = 1
Output: 0

Example 4:
Input: dividend = 1, divisor = 1
Output: 1
 

Constraints:
-2^31 <= dividend, divisor <= 2^31 - 1
divisor != 0
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """二分 + 倍增乘法"""
        MAX_VAL = 2 ** 31 - 1
        MIN_VAL = -2 ** 31
        x, y = dividend, divisor
        is_neg = (x < 0 and y > 0) or (x > 0 and y < 0)
        x = -x if x < 0 else x
        y = -y if y < 0 else y
        # 由于x/y的结果肯定在[0,x]范围内，所以对x使用二分法
        left, right = 0, x
        # 退出循环时，left == right
        while left < right:
            # +1是为了避免死循环。例如：left=0，right=1
            mid = left + right + 1 >> 1
            # 说明结果落在[mid, right]内
            if self.quick_multi(mid, y) <= x:
                left = mid
            else:
                right = mid - 1
        res = -left if is_neg else left
        return res if MIN_VAL <= res <= MAX_VAL else MAX_VAL

    def quick_multi(self, a: int, b: int) -> int:
        """快速乘法，采用了倍增的思想。得到两个非负整数的乘积"""
        res = 0
        while b > 0:
            if b & 1 == 1:
                res += a
            b >>= 1
            a <<= 1
        return res


if __name__ == '__main__':
    print(Solution().divide(-10, 3))
