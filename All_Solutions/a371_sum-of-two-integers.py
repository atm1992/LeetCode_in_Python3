# -*- coding: UTF-8 -*-
"""
title: 两整数之和
Given two integers a and b, return the sum of the two integers without using the operators + and -.


Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5


Constraints:
-1000 <= a, b <= 1000
"""


class Solution:

    def getSum(self, a: int, b: int) -> int:
        """
        位运算
        Python是没有位数这个概念的，它不会像其它语言那样将int认作32位，超出32位就溢出，Python不会溢出。所以需要手动模拟32位 INT 整型
        Python的第32位并不是它的最高位符号位，可将符号位认为是远大于32位的某一位。
        """
        # 第1位 ~ 第32位(下标0~31) 均为1。
        # & mask1 可将Python中的原始数据只保留(下标0~31)的低32位作为有效位，高于第32位之后(下标大于31)的位均变为0。
        # &操作会改变Python中远大于32位的那个符号位
        # mask1 = 2 ** 32 - 1
        mask1 = 0xFFFFFFFF
        # 下标为31的二进制位为1，其余位均为0。只有负数的第32位(下标为31)为1，所以可用来区分正负数
        # mask2 = 2 ** 31
        mask2 = 0x80000000
        # 只保留(下标0~31)的低32位作为有效位，并且我们人为认定第32位作为符号位，若第32位为1，则认为是负数。
        # 注意：对Python而言，第32位为1的数，也是正数。因为第32位并不是Python认为的符号位
        a &= mask1
        b &= mask1
        while b != 0:
            # a —— 不进位的相加结果；b —— 每一位的进位结果
            a, b = (a ^ b) & mask1, ((a & b) << 1) & mask1
        # 若最终结果为负数，即 最高位符号位(第32位)为 1
        if a & mask2:
            # a ^ mask3 将第1位 ~ 第32位(下标0~31) 按位取反；
            # 之后 ~ 再将第1位 ~ 第32位取反回来，只不过相比上面那步，此时取反的不只是(下标0~31)的低32位，
            # 还会将第32位之后(下标大于31)的所有位都取反，包括Python中远大于32位的那个符号位。
            # 总结一句话：将我们人为认定的32位负数(第32位为1) 转换回 Python认为的负数
            return ~(a ^ mask1)
        else:
            return a


if __name__ == '__main__':
    print(Solution().getSum(-2, -9))
