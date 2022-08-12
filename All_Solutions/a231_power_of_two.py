# -*- coding: UTF-8 -*-
"""
title: 2 的幂
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2^x.


Example 1:
Input: n = 1
Output: true
Explanation: 2^0 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 2^4 = 16

Example 3:
Input: n = 3
Output: false


Constraints:
-2^31 <= n <= 2^31 - 1

Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """位运算。2 的幂 的二进制表示中只有一位为1，其余位均为0。2 的无论多少次幂，都不可能为负数，负数次幂，结果也是正数"""
        # n & (n-1) 可以消去最低位的1，然而2 的幂只有一位为1，消去后，自然就会等于0
        return n > 0 and n & (n - 1) == 0

    def isPowerOfTwo_2(self, n: int) -> bool:
        """位运算"""
        # 正数的补码就是原码；负数的补码为绝对值的原码按位取反，然后加1
        # 例如：n = 000100，则 -n = 111011 + 1 = 111100，n & -n = 000100 = n
        return n > 0 and n & -n == n

    def isPowerOfTwo_3(self, n: int) -> bool:
        """题目给的条件是：n <= 2^31 - 1，因此在这个范围内，2 的幂最大为 2 ^ 30"""
        big_num = 2 ** 30
        return n > 0 and big_num % n == 0
