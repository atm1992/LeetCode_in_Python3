# -*- coding: UTF-8 -*-
"""
title: 不用加减乘除做加法
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。


示例:
输入: a = 1, b = 1
输出: 2


提示：
a, b 均可能是负数或 0
结果不会溢出 32 位整数
"""


class Solution:
    def add(self, a: int, b: int) -> int:
        """位运算。Python需要注意负数"""
        # 只操作输入数据的低32位，并将第32位(下标为31)看作符号位
        mask = 0xffffffff
        a, b = a & mask, b & mask
        while b != 0:
            # 分别为不进位相加的结果、进位结果
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # 若最终结果为负数，则将负数的补码还原至Python的存储格式
        return ~(a ^ mask) if a >> 31 else a


if __name__ == '__main__':
    print(Solution().add(a=-10, b=-19999))
